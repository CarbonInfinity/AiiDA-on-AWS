# AiiDA-on-AWS
This guide introduces you to setting up a high-performance compute cluster on [Amazon Web Services](https://aws.amazon.com/) (AWS) and managing calculations on it using the [AiiDA](https://www.aiida.net/) workflow manager.
Note: This guide has not yet been updated to aws-parralelcluster 3.0. Please use version 2.

## Sections
1. [Setting up a HPC cluster on AWS:](Section1/aws-cluster-setup.md)
Create your first HPC cluster and configure it to allow AiiDA to connect to it.
2. [Connecting AiiDA to the HPC:](Section2/connecting-aiida.md) connect to the cluster from an AiiDA docker container and run a first calculation. 
3. [Installing software on the cluster](Section3/installing-software.md)
4. [Advanced HPC clusters:](Section4/advanced-clusters.md) spot instances and how to add to the AiiDA docker container.

5. [Troubleshooting](Troubleshooting/Troubleshooting.md)


## Contributing
This project welcomes contributions to all parts of the repo. As an example almost all steps explained in the guide could be automated. Please raise an issue if you have a specific area you would contribute to.
