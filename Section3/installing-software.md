# Installing software on the AWS HPC
The following section will guide you through how to install software on your new HPC and how to then run a more advanced workflow. 

## Shared directories
Just like on most HPCs, the compute and head nodes share one or more directories. On a normal HPC you may use these shared directories to store the results of your calculations, the programs you are executing and the code you use to orchestrate them. As we are using AiiDA to manage our calculations this setup is a bit different. When you run a workflow with AiiDA, first a new workflow node is registered in the database. Then the files necessary for the calculation are prepared. E.g. for a Raspa calculation this may be the cif file of the structure, the input file for the raspa calculation and a short script which runs the calculation. If the calculation is run locally the script is executed and no further actions are necessary. However, for the HPC more steps are required. First the files are transferred from our docker container to the HPC. There the script is run and our simulation is started. Then after the simulation is finished the output is transferred back to the container. 

## HPC configuration

Within the HPC config file, the shared directories parameter is specified within the ebs section. This specifies the path where the shared Amazon EBS volume is mounted. 

```
[ebs myebs]
shared_dir = /shared
```



## Installing software
