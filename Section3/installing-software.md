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

- `shared_dir` Can be used to specify the path where the volume is mounted on both the head and compute nodes.
- `volume_size` Defines the size of the volume in gigabytes. In example above the volume would have 100 GB. The default size is 20 GB.
- `ebs_volume_id` Can be used to mount an already existing ebs volume. 
- `ebs_snapshot_id` Cimilarly to `ebs_volume_id` this keyword can be used to mount an existing snapshot of an ebs volume.
- `volume_type` Allows the user to choose a specific volume type. Available are:  
  - `gp2, gp3` General purpose SSDs
  - `io1, io2` Provisioned IOPS SSDs
  - `st1` Throughput optimized HDD

More information about configuring ebs volumes can be found [here](https://docs.aws.amazon.com/parallelcluster/latest/ug/ebs-section.html). Similarly the filesystem that is used by the head node can also be [configured](https://docs.aws.amazon.com/parallelcluster/latest/ug/efs-section.html). 

## Installing software

Installing software on the head node is very similar to installing software on your local computer with two caveats: 
1. You will have to ensure that the software is installed in the shared directory.
2. In light of the cost of running a HPC, small performance increases of the code become significant. As such we will compile the codes specifically for the processor type of our EC2 instances.

In the following we will examplary install RASPA 2.0. The same steps are appicable to most simulations codes.

### Installing RASPA
Open the provided `install_raspa` script. 

```
wget https://github.com/iRASPA/RASPA2/archive/v2.0.45.tar.gz
tar -xvf v2.0.45.tar.gz
cd RASPA2-2.0.45
mkdir m4
aclocal
autoreconf -i
automake --add-missing
autoconf
```
The above section downloads, extracts and prepares the installation of RASPA.

```
./configure CFLAGS="-march=cascadelake -O2 -pipe" CXXFLAGS="-march=cascadelake -O2 -pipe" --prefix=${PREFIX}
```

Using `./configure` we can add flags for the C compiler such that we compile for a specific processor type. In this case `cascadelake`. Next we finish the installation:

```
make
sudo make install 
sudo ldconfig
```

This finishes the installation of RASPA. However, the executable is not yet in a shared directory. As such we create a folder in `/shared` and copy our executable over:

```
mkdir /shared/Raspa
cp /bin/simulate /shared/Raspa/simulate
```

Now let's actuallly install RASPA. Login into the head node, add executive permissions to the script (`chmod +x <file name>`) and execute it (`./<file name>`). 
If everything goes well, you will now have installed RASPA. A similar script for Zeo++ is provided as well and using the above as a template you can create one for your simulation codes. Now move on to [section 4](../Section4/advanced-clusters.md).
