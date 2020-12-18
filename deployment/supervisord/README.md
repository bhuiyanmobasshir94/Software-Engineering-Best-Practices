Supervisor is a process manager which makes managing a number of long-running programs a trivial task by providing a consistent interface through which they can be monitored and controlled.
Celery is a task queue/job queue based on distributed message passing. It is focused on real-time operation but supports scheduling as well.
The execution units, called tasks, are executed concurrently on a single or more worker server. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
Celery is already used in production to process millions of tasks a day.
Celery is written in Python, but the protocol can be implemented in any language. It can also operate with other languages using webhooks.
Here, we are going to implement two of these together to get the best out of it.
First, install supervisor using apt-get package.
To run celery Redis-server is needed. So the following command would need.
sudo apt-get install redis-server
sudo systemctl enable redis-server.service
Write the following command to /etc/supervisor/conf.d/celery.conf
```
[program:celery]
directory = <django_project_directory> example:[/home/ubuntu/prod/api]
command = <virual_environment_directory/bin/celery> <command_to_be_executed> example: [/home/ubuntu/anaconda3/envs/api_env/bin/celery] [-A prodapi worker -l info --without-gossip --without-mingle --without-heartbeat -Ofair --pool=solo] 
stdout_logfile=/var/log/supervisor/celery.log 
stderr_logfile=/var/log/supervisor/celery.log
user=<username> example: [ubuntu]
```
Then to start it working write this command
supervisorctl restart celery
Thanks for the read. For reference please go through this link:
https://www.digitalocean.com/community/tutorials/how-to-install-and-manage-supervisor-on-ubuntu-and-debian-vps
https://django-celery.readthedocs.io/en/2.4/introduction.html
