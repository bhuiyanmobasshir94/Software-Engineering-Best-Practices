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

#### References
1. [Quickstart: Compose and Django](https://docs.docker.com/compose/django/)
2. [Django Development with Docker Compose and Machine](https://realpython.com/django-development-with-docker-compose-and-machine/)
3. [Welcome to Cookiecutter Django’s documentation!](https://cookiecutter-django.readthedocs.io/en/latest/index.html)
