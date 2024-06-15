# Ubuntu 20 64-bit deployment

---

> sudo apt update
> sudo apt upgrade

install vim

> sudo apt install vim

Enter the Home directory

> cd ~

Add "alias vi=vim" to bashrc

>vim.bashrc

Refresh takes effect bashrc

>source .bashrc

install git

>sudo apt install git

Download GreaterWMS from gihub

>sudo git clone https://gitee.com/Singosgu/GreaterWMS.git

install nodejs

>wget https://nodejs.org/dist/v14.18.3/node-v14.18.3-linux-x64.tar.gz
> tar zvxf node-v14.18.3-linux-x64.tar.gz -C /usr/local
> echo ''' export NODE_HOME=/usr/local/node-v14.18.3-linux-x64 export PATH=$PATH:$NODE_HOME/bin export NODE_PATH=$NODE_HOME/lib/node_modules''' /etc/profile

Make environment variables take effect immediately

>source /etc/profile
>sudo ln -sf /usr/local/node-v14.18.3-linux-x64/bin/node /usr/bin/node
>sudo ln -s /usr/local/node-v14.18.3-linux-x64/bin/npm /usr/bin/npm

Verify that node is installed successfully

>sudo node -v

Verify that npm is installed successfully

>sudo npm -v

- After this step is completed, you need to restart your Terminal, otherwise the upgrade will not take effect

> sudo npm install npm -g
> sudo npm install yarn -g
> sudo npm install -g @quasar/cli

Make sure your python version is above 3.8, in principle 3.6 is also possible, but there will be some problems with installing the library

> python3

Make sure you have pip3 installed

> pip3 list

If you don't have pip3, install it

> sudo apt install python3-pip

Check if the installation was successful

> pip3 list

Elevate GreaterWMS Folder

>sudo chmod -R 755 GreaterWMS

> cd GreaterWMS
> sudo pip3 install -r requirements.txt

Sometimes, you will have problems installing these libraries because of the python3 version. Don't worry, just sudo pip3 install the wrong library.

> sudo daphne -p 8008 greaterwms.asgi:application
> Now open the browser, enter "127.0.0.1:8008", you will see a 500 error, congratulations, you can deploy the next thing normally

Go back to the GreaterWMS folder

> Ctrl + C

Database generation and migration

> sudo python3 manage.py makemigrations
> sudo python3 manage.py migrate

Start GreaterWMS

> sudo daphne -p 8008 greaterwms.asgi:application
- Now open your browser, type "127.0.0.1:8008" and you will see the project is running
- Enter "127.0.0.1:8008/myip", you will get your intranet IP, be sure to remember it

Go back to the GreaterWMS folder

> Ctrl + C

Go to templates folder

> cd templates

Wait for the Yarn installation to complete. In fact, you can also sudo npm install , but it will be slower

> sudo yarn install

Start the front-end page with the quasar command

> sudo quasar d

- The front end will send a request to "127.0.0.1:8008", here we just check if the project can run

- Since version 2.0.19, the modification method of the request address has been optimized. By directly modifying the baseurl and wsurl in templates/dist/spa/statics/baseurl.js, you can successfully change the front-end request address, and you no longer need to do the following quasar build packaging works.
- If you need to modify the front-end content, you also need to modify the baseurl and wsurl in templates/public/statics/baseurl.js, and then re-use quasar build for packaging

>Press Esc and type ":wq" to save changes
>Now, you know how to deploy and modify the request address

Modifications need to be repackaged

> sudo quasar build

Go back to the GreaterWMS folder

> cd ..

Restart GreaterWMS

> sudo daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application

 Now, open a browser and enter "Intranet IP: 8008"