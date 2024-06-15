# Windows 10 64-bit deployment

---

Download python3.9.5 (the version is mainly based on your own computer system, we take 64-bit as an example)
> https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe

- Right click, run the exe file as administrator, install python3.9.5
- Be sure to check Add Python3.9 To PATH, then click Install Now

pip set permanent Alibaba cloud mirror source
> Go to the following address:
> C:\Users\{your username}\AppData\Roaming\ create a new pip folder
Create a file pip.ini in the pip folder and add the following:
>>
>> [global]
>> trusted-host = mirrors.aliyun.com
>> index-url = https://mirrors.aliyun.com/pypi/simple
>>
>Add system environment variable %HOME%\pip\pip.ini

Download sqlite3 (the version is mainly based on your own computer system, we take 64-bit as an example)

> https://www.sqlite.org/2021/sqlite-dll-win64-x64-3350500.zip

- Unzip the zip file, and the unzipped file will overwrite the file in the python path dll, the address is
~ C:\Users\{your username}\AppData\Local\Programs\Python\Python39\DLLs


Download Node.JS14.18.3 (the version is mainly based on your own computer system, we take 64-bit as an example)
> https://nodejs.org/dist/v14.18.3/node-v14.18.3-x64.msi

Download Git (the version is mainly based on your own computer system, we take 64-bit as an example, you need to download the 64-bit version)
> https://registry.npmmirror.com/binary.html?path=git-for-windows/

- Right click, run the exe file as an administrator, and then go to the next step
- Select which directory you want to put GreaterWMS in, right-click and select Git Bash Here

Download GreaterWMS code from gitee
> git clone https://gitee.com/Singosgu/GreaterWMS.git
- In the search bar in the lower left corner, enter cmd
- Right click and run cmd as administrator
- View Python version

> python -V

- Check if pip is installed
> pip list

Upgrade pip to the latest version
> pip install --upgrade pip

Enter the GreaterWMS placement directory, which is placed in downlowad during the demo, so we go into the directory
~ cd C:\Users\{your username}\Downloads\GreaterWMS\


pip install python dependency library
> pip install -r requirements.txt

Twisted may not be installed, you need to download it and install it manually

> https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted

- Download your own suitable version, for example: my demo video is Python3.9.5, and the Win10 version is 64-bit
- So I'm going to download Twisted-20.3.0-cp39-cp39-win_amd64.whl
- Place the downloaded Twisted in the root directory of GreaterWMS and install it manually

> pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl

run install requirements.txt
> pip install -r requirements.txt

Start GreaterWMS
> daphne -p 8008 greaterwms.asgi:application

- Now open the browser and enter 127.0.0.1:8008
- If you see an error of 500, it means that all previous Python dependencies have been installed


Go back to the CMD interface, hold down Ctrl+C to exit the project startup
Generate database migration files

> python manage.py makemigrations

Generate database

> python manage.py migrate

- start the project again
> daphne -p 8008 greaterwms.asgi:application

- Now open the browser and enter 127.0.0.1:8008
- View LAN IP, browser input 127.0.0.1:8008/myip
- Save or remember this IP address
- It must be noted that the intranet IP obtained by windows is different every time you start up. Either you set a fixed intranet IP to this computer on your router, or you don't turn off the computer.

Go back to the CMD interface, hold down Ctrl+C to exit the project startup
Go to the templates directory

> cd templates

- Since version 2.0.19, the modification method of the request address has been optimized. By directly modifying the baseurl and wsurl in templates/dist/spa/statics/baseurl.js, you can successfully change the front-end request address, and you no longer need to do the following quasar build packaging works. If you need to modify the front-end content, you also need to modify the baseurl and wsurl in templates/public/statics/baseurl.js, and then re-use quasar build for packaging

upgrade npm

> npm install -g npm

Install Yarn
> npm install -g yarn


Install the quasar environment

> npm install -g @quasar/cli

Install the windows build tools Note: If you can't install it, please download Visual Studio to install the C++ environment

> npm install -g windows-build-tools

Install core-js dependencies

> npm install -g core-js

Check if global dependencies are installed

> npm list -g --depth=0

Install project dependencies
> yarn install

- This process will be a bit slow, sometimes very fast, because the network is blocked
- If an error occurs, it is blocked due to network reasons. We provide a downloaded front-end dependency, and you can download it.

Download front-end dependencies

> git clone https://gitee.com/cow111023/node_modules.git

If it is a LAN deployment, change 127.0.0.1 to the intranet IP you just checked

> const baseurl = 'http://127.0.0.1:8008/'
> const wsurl = 'ws://127.0.0.1:8008/'

- save and exit

Recompile the front end in the templates directory
> quasar build

Go back to the GreaterWMS root directory


> cd ..

Add the -b 0.0.0.0 parameter to the startup project
> daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application

- Next, you can use your browser to visit { http://intranet IP:8008 } to view the project
- Computers on the LAN can also access the project through this IP