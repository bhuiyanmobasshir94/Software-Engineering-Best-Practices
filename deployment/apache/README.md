After doing an excellent project we often float in big thoughts on how to do the deployment and where. As a noob, this kills our time a lot. That’s why I wanted to find a way how I can deploy any Django project easily.
I have used Amazon EC2 instance — t2.micro, p2.xlarge and g3s.xlarge with ubuntu 16.04 distribution of the Linux operating system. But you can do the same to any cloud with a Linux operating system.
To setup, Apache follows this URL. This is a well-written blog from Digital Ocean.

To install environment dependent (within python virtual environment)mod-wsgi do the following within your activated environment setup:
```
sudo apt-get install apache2-dev
pip install mod-wsgi
```
Get the environment variable from this command and set it to the apache config file(/etc/apache2/apache2.conf) ( paste it at the last):
```
mod_wsgi-express module-config
```
Check the apache config test and if it says syntax ok then you are good to go:
```
sudo apache2ctl configtest
```
Now we have to set several permissions for different folders including project folder, media folder, static folder and also for default database DB.sqlite3 (if you are using it).
The project directory that holds manage.py file have to give permissions and also change ownership :
```
sudo chmod 775 <project_folder_name>
sudo chown :www-data <project_folder_name>
```
Database SQLite has to do the same (if you use this in production):
```
sudo chown ubuntu:www-data db.sqlite3
sudo chmod g+w db.sqlite3
```
For serving media and static files in production, it is a good practice that we serve it from /var/www. This is preferred and said way. So we have to make a directory there.
```
mkdir <project_folder_name>
```
To configure the project directory that holds media and static:
```
sudo chown www-data:www-data -R <project_folder_name>
cd <project_folder_name>
```
Create media and static folder in the directory using the same mkdir command.
To change ownership and give permissions have to do the following to static/media folders:
```
sudo chown ubuntu:www-data -R media
sudo chmod g+w media
sudo chown ubuntu:www-data -R static
sudo chmod g+w static
```
To configure the default configuration file at /etc/apache2/sites-available/000-default.conf (past it at the last before <virtualhost>):
```
Alias /static/ /var/www/<project_folder_name>/static/
<Directory /var/www/<project_folder_name>/static>
Require all granted
</Directory>
Alias /media/ /var/www/<project_folder_name>/media/
<Directory /var/www/<project_folder_name>/media>
Require all granted
</Directory>
<Directory <path_to_django_project_folder_app_name>>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
WSGIDaemonProcess <arbitrary_name> python-home=<path_to_virtual_env> python-path=<path_to_django_project_directory>
WSGIProcessGroup <arbitrary_name>
WSGIScriptAlias / /<path_to_>wsgi.py
```
Make sure that the file has these permission set in /var/www directory:
```
drwxr-xr-x => <project_directory>
drwxrwx--- => media
drwxrwx--- => static
-rw-rw-r-- => <file_in_media_and_static>
```
And to do that we have to do the following:
To know which user you are logged on to:
```
$ whoami
>> ubuntu
```
And adding to your solution, if you are using an AWS Instance, you should add your user to the group to be able to access that folder:
Making a group for webservices users (varwwwusers)
```
$ sudo groupadd varwwwusers
```
Change the www folder and make it belong to varwwwusers
```
$ sudo chgrp -R varwwwusers /var/www/
```
www-data is the server making Django requests, add that to the group
```
$ sudo adduser www-data varwwwusers
```
Change folder policy
```
$ sudo chmod -R 770 /var/www/
```
Add ubuntu to the group of varwwwusers
```
$ sudo usermod -a -G varwwwusers ubuntu
$ sudo usermod -a -G varwwwusers www-data
```
OR
```
sudo groupadd varwwwusers
sudo adduser www-data varwwwusers
sudo chgrp -R varwwwusers /var/www/
sudo chmod -R 760 /var/www/
```
To restart Apache server:
```
sudo /etc/init.d/apache2 restart
```
You are now good to go.
To see the access log as you see in Django development server console:
```
sudo tail -f /var/log/apache2/access.log
```
To see the error log if any error happens in the server end:
```
sudo tail -f /var/log/apache2/error.log
```
Hope this helped you to get some basic ideas. I tried to keep it short and concise so that your workload can be minimized.
Thank you for your read.

Reference:
https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-debian-8
https://stackoverflow.com/questions/21797372/django-errno-13-permission-denied-var-www-media-animals-user-uploads
http://www.tobiashinz.com/2019/04/10/apache-django-virtualenv.html
https://askubuntu.com/a/504525
