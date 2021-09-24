# Advanced settings

The following examples show how the set up may be modified to update the cluster for user specific applications.

## Extending the HPC config file

The following configuration parameters may be used to update the HPC for use with high throughput simulations. Following step 3h of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html), the config file may be updated. The configuration may be specified using [configuration parameters](https://docs.aws.amazon.com/parallelcluster/latest/ug/cluster-definition.html).

### Spot Instances
AWS [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) take advantage of unused EC2 instances. They are typically cheaper to run than on-demand instances and are useful for workflows which may be interupted. 

Similar to step 2f of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) outlined in Section 1.1 of this guide for on-demand EC2 instances, a spot instance should first be created manually by following the tutorial on creating a [Spot Instance request (console)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#using-spot-instances-request). This only needs to be done once during the set up stage to create a template for future spot instance requests. 

The config file can be updated to run on spot instances. With: 

```
[cluster default]

queue_settings = compute
```
The following parameters are needed in the config file to run on spot instances: 

```
[queue compute]

compute_type = spot

[compute_resource default]

spot_price = 0.25
```
Here spot price has been set to $0.25, see [default spot instance prices](https://aws.amazon.com/ec2/spot/pricing/) for each region. The instance will not be created unless the spot price falls below this threshold. If a value is not specified, it is set to the regional spot price and capped at on-demand.   

### Instance Type

The `master_instance_type` and `instance_type` define the Amazon EC2 instance type used for the head node and computer nodes respectively. The architecture of the instance type must be the same as the architecture used for the master_instance_type setting. These parameters are used if the queue_settings setting is defined. As the cluster we've been defined so far used relatively small c5.large instances upgrading the [instance type](https://aws.amazon.com/ec2/instance-types/) to e.g. c5.12xlarge vastly increases it's capabilities. 

Further useful information on AWS ParallelCluster can be found [here](https://jiaweizhuang.github.io/blog/aws-hpc-guide/) and [here](https://docs.aws.amazon.com/parallelcluster/latest/ug/parallelcluster-version-2.html)


## Extend the aiida-core dockerfile

The aiida-core dockerfile may be extended to include one's own modifications.

After following step 2.1.1. `Pull the docker container: docker pull aiidateam/aiida-core:latest`

You can run a shell in the image with: `docker run -t -i --entrypoint bash aiidateam/aiida-core:latest`

Then change the configuration files as you like. Note the container ID (it appears in the prompt, e.g. root@9ffa2bafe2bb:/#), then commit it to a new image: `docker commit 9ffa2bafe2bb aiida-core:newupdate`


