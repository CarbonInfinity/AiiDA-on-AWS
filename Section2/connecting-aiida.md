# Connecting AiiDA to the cluster
There are many options as to how AiiDA can be run. 
In the following we will run AiiDA inside a docker container running on our separate cloud9 instance (virtual machine). 

Other options include:
 * installing AiiDA natively in the same VM (e.g. using [this](https://galaxy.ansible.com/marvel-nccr/aiida) ansible role)
 * running the AiiDA docker container on your local machine
 * installing AiiDA natively on your local machine

Running AiiDA in the cloud has the advantage that the AiiDA daemon is "always on", and can therefore always keep advancing the running calculations.
Using docker makes it easy to spin up and tear down reproducible AiiDA environments but makes it more difficult to modify the environment on the go.

## 2.1. Downloading and configuring the AiiDA container
Before we start connecting AiiDA with our HPC we need to setup and configure the container from which we will be running AiiDA. Depending on your configuration, your volume may be too small to download the container. See [troubleshooting](../Troubleshooting/Troubleshooting.md) to resolve this.

To start:
1. Pull the docker container: `docker pull aiidateam/aiida-core:latest`  
2. Create a volume to associate with the container: `docker volume create aiida-data`
3. Launch to container: `docker run -d --name aiida-container --mount source=aiida-data,target=/home/aiida aiidateam/aiida-core:latest`
4. Enter into the container: `docker exec -it --user aiida aiida-container /bin/bash`

We have now a container running AiiDA. To verify that everything works as it should you can run `verdi status` (it takes about a minute for everything to boot). The aiida user currently has very few privileges making file handling challenging. 

To change this:
1. Exit the container
2. Reenter as root: `docker exec -it --user root aiida-container /bin/bash`
3. Change the root password: `passwd`
4. Give the AiiDA user ownership to `/home` (or the directory where your volume is located): `chown -R aiida /home`
5. Exit and reenter as aiida
6. Verify everything still works: `verdi status`

Our container is now ready to connect to the HPC cluster.

## 2.2. Connecting to the HPC 
We will now connect from the container to the HPC cluster using ssh. In this section it helps to have two terminals open. One for the container and one for the standard cloud9 instance. 

1. Copy the rsa key over to the container. 
2. Change it's permissions: `chmod 600 <key>`
3. Connect to the cluster again: `ssh ec2-user@<Master public ip> -i <path to key>`

Now we can connect to our HPC cluster from the terminal. The next step is to connect AiiDA to the cluster.

## 2.3 Connecting AiiDA to the HPC 
Next we will setup an AiiDA computer instance in our container to allow connecting to the HPC.

1. Clone the three files (`computer-setup.yaml`, `computer-config.yaml` and `add.yaml`) in the folder associated with this section into `/home/aiida/setup/`
2. Add your Master public ip to `computer-setup.yaml`
3. Setup up the computer: `verdi computer setup --config computer-setup.yaml`
4. Edit `computer-config.yaml` to reflect the correct path to the key with open permissions
5. Configure the the computer: `verdi computer configure ssh hpc --config computer-setup.yaml`
6. Choose the default (hit enter) for all other options
7. Run: `verdi computer list`. You should now see `hpc` in your computer list.
8. Run: `verdi computer test hpc`

If the tests pass - congratulations! 
You have now setup and configured AiiDA to interface with the HPC. Next up is running a job on the HPC through AiiDA.

## 2.4 Running a job through AiiDA on the HPC
To run code on our HPC we first need to setup a code for doing so. In this section we will use the add example AiiDA provides to verify that AiiDA works with the HPC.

1. To setup the code run: `verdi code setup --config add.yaml`
2. Verify that the code has been added: `verdi code list`
3. We are now going to run test.py, which will simply add two numbers together. To execute the script run: `verdi run test.py --add_code add@hpc`

You should now see how 0, 1, and 2 are added together. If so you have successfully run your first AiiDA script on the HPC.

You can now move on to the [next section](../Section3/installing-software.md) where we will be covering the installation of proper simulation codes.
