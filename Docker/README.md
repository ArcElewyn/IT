# Docker

## Chapter 1: Installation 
*I'm installing Docker on a Debian-12 system, so it might be different based on your OS*

#### 1. First I install the dependency needed for Docker to work properly:

> apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common

#### 2. Then I get the GPG key that we are gonna use to verify the packages we get from the docker's depot

> curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

#### 3. Next I add the Docker's depot to my apt sources

>echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list

> apt update

#### 4. Now it's time to install Docker itself 

> apt install docker-ce docker-ce-cli containerd.io

To check if it worked

> systemctl status docker

If status is not running, start the service, then, to verify if docker is working as intended, run

> docker run hello-world

## Chapter 2: Commands
*source: https://docs.docker.com/reference/cli/docker/* \
To display help, run:
> docker --help

To list the containers on your system, run:
> docker ps -a

To list only the active containers, run
> docker ps

To delete a container, run
> docker rm "container_ID"

To start or stop a container, run
>docker start/stop "container_ID"

To list available images, run
> docker images

To delete an image, first stop and delete the linked container then run:
> docker rmi "Name_of_the_image"

To pull a container from Docker Hub
> docker pull "name_of_the_container"

To build a container image, run \
*add option -t to use a custom name*
> docker build -t "image_name"

To run a container from an image, run \
*add option -d to run the container in background -p to set the ports of the container*
> docker run  -d -p "host_port":"container_port" "Container_ID"

To interact with the shell of the container, run
> docker exec "container_ID" bash

## Chapter 3: Docker-compose
*Docker compose is an orchestration tool that help running multi-contrainer apps* \
First we need to have Docker-compose on our system, to verifiy if so, run
> docker compose version

If it isn't installed yet, run
> apt install docker-compose-plugin

Then we can write our docker-compose.yml
> touch docker-compose.yml \
vi docker-compose.yml

To run our docker-compose, go in the directory where the .yml is and run
> docker compose up
