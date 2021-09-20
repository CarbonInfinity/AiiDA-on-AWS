# Spot Instances
AWS [Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) take advantage of unused EC2 instances. They are typically cheaper to run on than on-demand instances and are useful for workflows which may be interupted. 

Similar to step 2f of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) for on-demand EC2 instances, a spot instance should first be created manually by following the tutorial on creating a [Spot Instance request (console)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html#using-spot-instances-request). This only needs to be done once during the set up stage to create a template for future spot instance requests. 

Following step 3h of the [AWS ParallelCluster tutorial](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) outlined in Section 1.1 of this guide, the config file may be updated to run on spot instances. 

