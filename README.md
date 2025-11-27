# xCAT-docker-container-rocky9.4
This xCAT Docker image is built on Rocky Linux 9.4 and is fully supported for single-node xCAT management deployments. **With additional configuration, this image also supports a full xCAT High-Availability (HA) setup using: Docker Swarm, PCS (Pacemaker/Corosync) &amp; DRBD**

# Prerequisite: Install Rocky Linux 9.4 Base Image

Before building the xCAT container image, you must install the Rocky Linux 9.4 base image into your environment.

🏁 **Step 1: Install Rocky Linux 9.4 Base Image**

Use the GitHub repository to download and install the Rocky Linux 9.4 base image.

# Follow this GitHub link to install the Rocky Linux 9.4 base image
**This step is mandatory before building the xCAT container image.**


```
https://github.com/OpenHPC-AI/rocky-linux-container-base-image-el9
```


📌 **Why this is required?**

The xCAT container build is based on the Rocky Linux 9.4 minimal root filesystem.
Without installing this base image, the subsequent build steps will fail.

✔️ **After installing the base image**

Once the Rocky Linux 9.4 base image is available in your environment,
you may proceed with building the xCAT container image as described in the next steps of this documentation.
