# Installing software on the AWS HPC
The following section will guide you through how to install software on your new HPC and how to then run a more advanced workflow. 

## Shared directories
Just like on most HPCs, the compute and head nodes share one or more directories. On a normal HPC you may use these shared directories to store the results of your calculations, the programs you are executing and the code you use to orchestrate them. As we are using AiiDA to manage our calculations this setup is a bit different. When you run a workflow with AiiDA, first a new workflow node is registered in the database. Then the files necessary for the calculation are prepared. E.g. for a Raspa calculation this may be the cif file of the structure, the input file for the raspa calculation and a short script which runs the calculation. If the calculation is run locally this script is executed and no further actions are necessary. However, for the HPC more steps are required. First the files are transferred from our docker container to the HPC. There the script is run and our simulation is started. Then after the simulation is finished the output is transferred back to the container. 

## HPC configuration

Within the HPC config file, we can specify what how our shared directories are structured. Using the `[ebs <name>]` keyword we can indicate the start of a shared directory section.

```
[ebs ebs1]
shared_dir = /shared
volume_size = 100
```

As an example the above snippet defines an ebs volume called ebs1. An explanation of the most useful keywords can be found below. Of these only `shared_dir` is required.

- `shared_dir` can be used to specify the path where the volume is mounted on both the head and compute nodes.
- `volume_size` defines the size of the volume in gigabytes. In example above the volume would have 100 GB. The default size is 20 GB.
- `ebs_volume_id` can be used to mount an already existing ebs volume. 
- `ebs_snapshot_id` similarly to `ebs_volume_id` this keyword can be used to mount an existing snapshot of an ebs volume.
- `volume_type` allows the user to choose a specific volume type. Available are:  
  - `gp2, gp3` general purpose SSDs
  - `io1, io2` provisioned IOPS SSDs
  - `st1` Throughput optimized HDD

More information about configuring ebs volumes can be found [here](https://docs.aws.amazon.com/parallelcluster/latest/ug/ebs-section.html). Similarly the filesystem that is used by the head node can also be [configured](https://docs.aws.amazon.com/parallelcluster/latest/ug/efs-section.html). 

## Installing software
