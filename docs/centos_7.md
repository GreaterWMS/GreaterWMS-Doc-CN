# Centos 7 64-bit deployment

---

Enter the administrator account
>su -
>yum update
>yum upgrade

Install system dependencies

> yum -y install gcc-c++

Install Python dependencies

> yum install zlib-devel xz-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make

Install Node

> wget https://nodejs.org/dist/v14.19.3/node-v14.19.3-linux-x64.tar.gz
> tar zvxf node-v14.19.3-linux-x64.tar.gz -C /usr/local

Environment variable settings

> echo '''export NODE_HOME=/usr/local/node-v14.19.3-linux-x64 export PATH=$PATH:$NODE_HOME/bin export NODE_PATH=$NODE_HOME/lib/node_modules''' /etc/profile

Make environment variables take effect immediately

>source /etc/profile

Soft connection Node and NPM

> ln -sf /usr/local/node-v14.19.3-linux-x64/bin/node /usr/bin/node
> ln -s /usr/local/node-v14.19.3-linux-x64/bin/npm /usr/bin/npm

Verify that node is installed successfully

> node -v

Verify that npm is installed successfully

> npm -v

upgrade npm

> npm install npm -g

install yarn

> npm install yarn -g

install quasar

> npm install @quasar/cli -g

install cordova

> npm install cordova -g

check quasar version
> quasar -v

Upgrade sqlite3 version
> It is recommended to do this step before installing python3.9.5
>Download the source code
>wget https://www.sqlite.org/2019/sqlite-autoconf-3300100.tar.gz
> unzip, compile
>tar zxvf sqlite-autoconf-3290000.tar.gz
>cd sqlite-autoconf-3290000/
> ./configure --prefix=/usr/local
>make && make install
>Replace system low version sqlite3
>mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
>ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3
>echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
>ldconfig
>sqlite3 -version

Check python version

> python3

- If the python version is not 3.9.5, please execute the following command

> cd /usr/src
> wget https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz
> tar -zxvf Python-3.9.5.tgz
> cd Python-3.9.5/
> ./configure --enable-optimizations
> make altinstall
> mv /usr/bin/python3 /usr/bin/python3.bak
> ln -s /usr/local/bin/python3.9 /usr/bin/python3
> mv /usr/bin/pip3 /usr/bin/pip3.bak
> ln -s /usr/local/bin/pip3.9 /usr/bin/pip3

Check pip3 list is installed successfully

> pip3 list

install git

> yum install git

Download GreaterWMS from gitee

> git clone https://github.com/Singosgu/GreaterWMS.git

Elevate GreaterWMS Folder

> chmod -R 755 GreaterWMS

Go to the GreaterWMS folder

> cd GreaterWMS>pip3 install -r requirements.txt

- Sometimes, there will be problems when you install these libraries because of the python3 version, don't worry, pip3 install the wrong library.

> Ctrl + C

database generation

> python3 manage.py makemigrations // database generation

database migration

> python3 manage.py migrate // database migration

> /usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application

- Now open your browser, type "your external ip :8008" and you will see the project is running

Go back to the GreaterWMS folder

> Ctrl + C
> cd templates

Wait for the Yarn installation to complete. In fact, you can also npm install it, but it will be slower
Change yarn to domestic source
> /usr/local/bin/yarn install

Start the front-end page with the quasar command

> /usr/local/bin/quasar d

- The front end will send a request to "127.0.0.1:8008", here we just check if the project can run

Go back to the baseurl folder

> Ctrl + C // go back to templates folder
> ## Example changes before
> const baseurl = 'http://127.0.0.1:8008/'
> const wsurl = 'ws://127.0.0.1:8008/'
> 
> ## Example changes after
> const baseurl = 'https://{ your external ip }/'
> const wsurl = 'ws://{ your external ip }/'

- Press Esc and type ":wq" to save changes
- Now, you know how to deploy and modify the request address

back to templates
> ## you should build it again
> cd templates
> /usr/local/bin/quasar build

Go back to the GreaterWMS folder

> cd ..
> /usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
- Now, open the browser, type "your external IP: 8008", you can see the project is running