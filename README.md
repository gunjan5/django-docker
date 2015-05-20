# django-docker
Django+SQLite3 with Docker
http://gunjan5.github.io/django-docker/

### Welcome to Django+SQLite with Docker
I'm attempting to create Django based web backend with SQLite3 database using Docker.

To run the project, you need to have Docker and Docker Compose installed.

Once Docker and Docker Compose is installed, run the following command:

```
$ cd django-docker
$ docker-compose up
```

To start the containers in demon mode, use the following command instead:
```
$ docker-compose up -d
```

### Project Architecture
There are two Docker containers linked with each other in this project:
1. web (for django files) 
2. db (for sqlite3 database)
When you run _docker-compose up_, it builds these containers from **Dockerfile**, links them, installs the dependancies and starts the django apps.

### Pages
Once the containers are running, you just have to get the docker IP (localhost or if you're running docker in boot2docker for mac or inside a VM then VM/boot2docker's IP, please keep in mind it has to be NATed/Bridged properly for this to function)

Then go to browser and type in the IP and port 8000:
```
<IP-ADDRESS>:8000
```
Some pages for the site are:
```
<IP-ADDRESS>:8000/myadmin
<IP-ADDRESS>:8000/html
<IP-ADDRESS>:8000/fancy
<IP-ADDRESS>:8000/ttt
(more to come)
```

### Author
Gunjan Patel (@gunjan5)

### Contact
@Gunjan_Patel1
