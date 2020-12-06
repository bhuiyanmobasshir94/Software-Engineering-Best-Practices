## Commands

##### RUN - Start a container
```
docker run nginx
```
##### PS - List Containers
```
docker ps
docker ps -a
```
##### STOP - Stop a container
```
docker stop <name or id of the container>
```
##### RM - Remove a container
```
docker rm <name or id of the container>
```
##### IMAGES - List images
```
docker images
```
##### RMI - Remove images
```
docker rmi nginx
```
##### PULL - Download an image
```
docker pull nginx
```
##### Append a command
```
docker run ubuntu sleep 5
```
##### EXEC - Execute a command
```
docker exec <name or id of the container> cat /etc/hosts
```
##### RUN - Attach and detach
```
docker run <name>
docker run -d <name>
docker attach <id of the container>
```
##### RUN - Tag
```
docker run redis:<tag_name>
```
##### RUN - STDIN
```
docker run -i redis:<tag_name>
docker run -it redis:<tag_name>
```
##### RUN - PORT mapping
```
docker run -p <docker_host_port>:<Container_port> <web_app_name>
```
Every container will have unique internal <ip address> and port number. We must route to containers from docker host's external <ip_address> and <port_number> 
  
##### RUN - VOLUME mapping
```
docker run -v <docker_host_volume>:<Container_volume> <web_app_name>
```
##### Inspect container
```
docker inspect <name or id of the container>
```
##### Container logs
```
docker logs <name or id of the container>
```
##### Environment variables
```
docker run -e <set_environment_variables> <name of the container>
```
##### How to create my own image?
1. OS - Ubuntu
2. Update apt repo
3. Install dependencies using apt
4. Install python dependencies using pip 
5. Copy source code to `/opt` folder
6. Run the web server using `flask` command

```
FROM Ubuntu
RUN apt-get update
RUN apt-get install python

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/src

ENTRYPOINT FLASK_APP=/opt/src/app.py flask run 
```
```
docker build Dockerfile -t <name of the container>
docker push <name of the container>
```
```
docker history <name of the container>
```
```
docker build .
```
##### CMD vs ENTRYPOINT
```
CMD command param1
CMD ["command", "param1"]
```
```
FROM Ubuntu
CMD sleep 5
```
```
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper
```
```
FROM Ubuntu
ENTRYPOINT ["sleep"]
```
```
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper 10
```
`CMD` executes the whole command but `ENTRYPOINT` gives an initializer for the command
```
FROM Ubuntu
ENTRYPOINT ["sleep"]
CMD ["5"]
```
```
docker build -t ubuntu-sleeper .
docker run ubuntu-sleeper
```
It will take the command from `ENTRYPOINT` and parameter value from `CMD` unless nothing provided in `docker run`.

```
docker run --entrypoint <command_name> <name of the container> <command_param_value>
```
If so then value of the `--entrypoint` will be replaced by default `ENTRYPOINT` command in `Dockerfile`

##### Default networks

1. Bridge - default network provided to all the containers inside docker host from series `172.17.x.X`
2. None - Container without any network
3. Host - If we want to access any container from outside the docker host and can't create multiple container with same port number as it hold back both internal and external port.

```
docker run <name of the container> --network=<network_name>
```
User defined network
```
docker network create --driver bridge --subnet 182.18.0.0/16 <custom-isolated_network_name>
```
```
docker network ls 
```
##### Embedded DNS
DNS server address `127.0.0.11`

##### File System

- /var/lib/docker
  - aufs
  - containers
  - image
  - volumes
  
##### Layered architecture
```
Image layer (read-only) -> Container layer (read-write)
```
##### Volumes

Volume mounting:
```
docker volume create <volume_name>
```
- /var/lib/docker
  - aufs
  - containers
  - image
  - volumes
    - <volume_name>
```
docker run -v <volume_name>:/var/lib/mysql mysql
```
Bind mounting:
```
docker run -v <any_directory_inside_docker_host>:/var/lib/mysql mysql
```
or 
```
docker run --mount type=bind,source=<any_directory_inside_docker_host>,target=/var/lib/mysql mysql
```
Here source - location on docker host, targer - location on container

##### Storage drivers

- AUFS
- ZFS
- BTRFS
- Device mapper
- Overlay
- Overlay2

##### Docker compose
```
docker run -d --name=redis redis
```
```
docker-compose up
```
##### Deploy private registry
```
docker run -d -p 5000:5000 --name registry registry:2
docker image tag my-image localhost:5000/my-image
docker push localhost:5000/my-image
docker pull localhost:5000/my-image
docker pull 192.168.56.100:5000/my-image
```
##### Docker engine

Docker deamon -> REST API -> Docker CLI
```
docker -H=<remote-docker_engine>:<port_number> <other usual commands>
```
###### Cgroups
```
docker run --cpu=.5 ubuntu
docker run --memory=100m ubuntu
```
##### Container Orchestration
```
docker service create --replicas=100 nodejs
```

#### References
1. [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
2. [Django Development with Docker Compose and Machine](https://realpython.com/django-development-with-docker-compose-and-machine/)
3. [Welcome to Cookiecutter Django’s documentation!](https://cookiecutter-django.readthedocs.io/en/latest/index.html)
4. [Docker Tutorial for Beginners - A Full DevOps Course on How to Run Applications in Containers](https://www.youtube.com/watch?v=fqMOX6JJhGo&t=1262s)
