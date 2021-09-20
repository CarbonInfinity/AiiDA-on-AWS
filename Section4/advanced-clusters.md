# Spot Instances
AWS [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) take advantage of unused EC2 instances. They are typically cheaper to run on than on-demand instances and are useful for workflows which may be interupted. 

Similar to step 2f of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) outlined in Section 1.1 of this guide for on-demand EC2 instances, a spot instance should first be created manually by following the tutorial on creating a [Spot Instance request (console)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#using-spot-instances-request). This only needs to be done once during the set up stage to create a template for future spot instance requests. 

Following step 3h of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html), the config file may be updated to run on spot instances. The configuration may be specified using [configuration parameters](https://docs.aws.amazon.com/parallelcluster/latest/ug/cluster-definition.html). An example config file for spot instances (here spot price has been set to $0.25, see [default spot instance prices](https://aws.amazon.com/ec2/spot/pricing/) for each region): 

```
cat > my-cluster-config.ini << EOF
[aws]
aws_region_name = ${REGION}

[global]
cluster_template = default
update_check = false
sanity_check = true

[vpc public]
vpc_id = ${VPC_ID}
master_subnet_id = ${SUBNET_ID}

[cluster default]
key_name = lab-3-your-key
base_os = alinux2
scheduler = slurm
master_instance_type = c5.xlarge
s3_read_write_resource = *
vpc_settings = public
ebs_settings = myebs
queue_settings = compute

[queue compute]
compute_resource_settings = default
disable_hyperthreading = true
placement_group = DYNAMIC
compute_type = spot

[compute_resource default]
instance_type = c5.2xlarge
min_count = 0
max_count = 12
spot_price = 0.25

[ebs myebs]
shared_dir = /shared
volume_type = gp2
volume_size = 100

[aliases]
ssh = ssh {CFN_USER}@{MASTER_IP} {ARGS}
EOF
```


A further useful [reference on AWS ParallelCluster](https://jiaweizhuang.github.io/blog/aws-hpc-guide/)
