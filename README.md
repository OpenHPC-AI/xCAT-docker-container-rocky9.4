# xCAT-docker-container-rocky9.4
This xCAT Docker image is built on Rocky Linux 9.4 and is fully supported for single-node xCAT management deployments. **With additional configuration, this image also supports a full xCAT High-Availability (HA) setup using: Docker Swarm, PCS (Pacemaker/Corosync) &amp; DRBD**

**Prerequisite: Install Rocky Linux 9.4 Base Image**

Before building the xCAT container image, you must install the Rocky Linux 9.4 base image into your environment.

🏁 **Step 1: Install Rocky Linux 9.4 Base Image**

Use the GitHub repository to download and install the Rocky Linux 9.4 base image.

**Follow this GitHub link to install the Rocky Linux 9.4 base image.**
***This step is mandatory before building the xCAT container image.***


```
https://github.com/OpenHPC-AI/rocky-linux-container-base-image-el9
```


📌 **Why this is required?**

The xCAT container build is based on the Rocky Linux 9.4 minimal root filesystem.
Without installing this base image, the subsequent build steps will fail.

Once the Rocky Linux 9.4 base image is available in your environment,
you may proceed with building the xCAT container image as described in the next steps of this documentation.

🏁 **Step 2:  Build xCAT docker container image based on rocky9.4**

**Copy xcat docker container image code in to your env.**

```bash
# git clone the code in your environment
git clone https://github.com/OpenHPC-AI/xCAT-docker-container-rocky9.4.git
```
**Build xCAT Contanier Image**

```bash
cd xCAT-docker-container-rocky9.4
docker build --network host  -t xcat_rocky9.4:2.17.0 .
```
✅ **Once the xCAT container image is built successfully, verify it.**

```bash
docker images | grep xcat_rocky9.4:2.17.0
```

🏁 **Step 3: Create the xCAT Container on a Single Server Node**

```bash
cd portable

# Update the dev.env file for your environment, then copy it to .env
cp dev.env .env

# After updating the environment file, create the container using run.sh
# Modify the run.sh file to reflect the hostname and container name specific to your environment.
bash run.sh

```
✅ **Verify the xCAT Container**

```bash
docker ps | grep xcat

# Verify that the xCAT service is up and running
docker exec -it <xcat-container-name> lsxcatd -a

```

Note:
By default, xCAT uses SQLite as its backend database.
However, this container is configured to use MySQL for improved performance and reliability.
