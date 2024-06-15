Using greaterwms under docker (this document is applicable to users with docker Foundation)


1.Install Or upgrade Docker Client
    wget -qO- https://get.docker.com/ | sh
    //If you are prompted that there is no curl, execute sudo apt install curl or yum -y install curl
    


2.Install Docker Compose
     curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose

3.Local trial
``
    docker run -itd --name greaterwms_v2.1.18 -p 8008:8008 -d greaterwms/greaterwms:v2.1.18
``

4.Install Git
    //Install git under Ubuntu
    apt-get install git
    //Installing git under CentOS
    yum install git

5.start deployment
//Pull code
git clone https://github.com/Singosgu/GreaterWMS.git
//Baseurl needs to be modified before running the project JS content
vim templates/public/statics/baseurl. JS / / modify 127.0.0.1 to the IP address of the server
//Nginx needs to be modified before running the project Contents of conf
vim nginx. conf / / change 127.0.0.1 to the local IP address. If deployed to a server, change to the server IP address
//Start project
docker-compose up -d
//Special note: after docker compose up -d is executed, the front-end dependencies will be automatically downloaded. Sometimes the download fails, causing the front-end to fail to start. At this time, docker compose down and then docker compose up -d are executed to download again until it succeeds.

6.release front-end code
//Enter the front container
docker exec -it greaterwms_ front_ v2.1.18 /bin/bash
//Enter the templates directory in the container
cd templates

//Compile front-end code

quasar build

7.view the supervisor access log
tail -f greaterwms_ server_ access. log
8.access portal
```
front end: http://127.0.0.1:8080 Or http:// server ip:8080
Back end: http://127.0.0.1:8008 Or http:// server ip:8008
nginx: http://127.0.0.1 Or http:// server IP