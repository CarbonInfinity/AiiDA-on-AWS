# 1. Setting up an AWS HPC Cluster

In this section you will get started with working on AWS, set up your first HPC cluster and then configure it to make it suitable for AiiDA. 

## 1.1. Creating the cluster
To get started follow the following tutorial on how to setup an [AWS Parallelcluster](https://www.hpcworkshops.com/03-hpc-aws-parallelcluster-workshop.html) until section 3h. The tutorial has not yet been updated to AWS Parallelcluster 3.0. As such please install the package using: `pip3 install "aws-parallelcluster<3.0" -U` Note: Do not delete the cluster as shown in 3i. We still need it :) 
The above tutorial uses an example config file containing the parameters needed to set up a HPC cluster, for further functionality refer to Section 4 ([Advanced HPC clusters](https://github.com/CarbonInfinity/AiiDA-on-AWS/blob/main/Section4/advanced-clusters.md)) or to the Parallelcluster [documentatation](https://docs.aws.amazon.com/parallelcluster/latest/ug/install.html).

If you already have an AWS HPC cluster and want to get started using it with AiiDA feel free to skip the above. 
You should now have a HPC cluster (deployed and managed using AWS Parallel Cluster) running and can connect to it using a Cloud9 environment. 

## 1.2. Configuring the cluster
Already back with more of an idea of how to create an HPC?

Now we will configure the cluster. Please open a terminal in your cloud9 instance.

To get an idea of how our cluster is doing run:
```
pcluster status hpclab-yourname
```
The output should look a bit like the following:
```
Status: CREATE_COMPLETE
MasterServer: RUNNING
MasterPublicIP: 52.23.18.144
ClusterUser: ec2-user
MasterPrivateIP: 172.31.82.247
ComputeFleetStatus: RUNNING
```
Particularly note down 
 * the master public ip
 * the ClusterUser (the default is `ec2-user`)

AiiDA connects to an HPC through ssh. In the standard configuration our HPC cluster does not allow connecting to the head node using normal ssh (e.g. `ssh ec2-user@<Master Public ip> -i <path to key>`). 

To change this:
1. From the Cloud9 terminal, log into the head node using the pcluster tool: `pcluster ssh <cluster name> -i <path to key>`
2. Open sshd_config with: `sudo nano /etc/ssh/sshd_config`
3. Ensure that `ChallengeResponseAuthentication` is set to `no` and `PasswordAuthentication` is set to `yes`
4. Restart the ssh service: `sudo systemctl restart sshd`
5. Exit the head node

Now back in our cloud9 environment we can try connecting to the head node:
```
ssh ec2-user@<Master public ip> -i <path to key>
```
Now you should be able to enter the head node.

If so, congratulations! Your HPC cluster is now configured and you are ready to connect AiiDA to it.

Move on to the next [section](../Section2/connecting-aiida.md).
