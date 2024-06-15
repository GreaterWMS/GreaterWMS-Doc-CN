# Centos 7 64位 部署

---

进入管理员账号
>su -
>yum update
>yum upgrade

安装系统依赖

> yum -y install gcc-c++

安装Python依赖

> yum install zlib-devel xz-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel libffi-devel gcc make

安装Node

> wget https://nodejs.org/dist/v14.18.3/node-v14.18.3-linux-x64.tar.gz
> tar zvxf node-v14.18.3-linux-x64.tar.gz -C /usr/local

环境变量设置

> echo '''export NODE_HOME=/usr/local/node-v14.18.3-linux-x64 export PATH=$PATH:$NODE_HOME/bin export NODE_PATH=$NODE_HOME/lib/node_modules''' /etc/profile

使环境变量立即生效

>source /etc/profile

软连接Node和NPM

> ln -sf /usr/local/node-v14.18.3-linux-x64/bin/node /usr/bin/node
> ln -s /usr/local/node-v14.18.3-linux-x64/bin/npm /usr/bin/npm

验证node是否安装成功

> node -v

验证npm是否安装成功

> npm -v

升级npm

> npm install npm -g

安装yarn

> npm install yarn -g

安装quasar

> npm install @quasar/cli -g

安装cordova

> npm install cordova -g

检查quasar版本
> quasar -v 

升级sqlite3版本
>建议在安装python3.9.5前就完成这一步
>下载源码
>wget https://www.sqlite.org/2019/sqlite-autoconf-3300100.tar.gz
>解压，编译
>tar zxvf sqlite-autoconf-3290000.tar.gz
>cd sqlite-autoconf-3290000/
>./configure --prefix=/usr/local
>make && make install
>替换系统低版本sqlite3
>mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
>ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3
>echo "/usr/local/lib" > /etc/ld.so.conf.d/sqlite3.conf
>ldconfig
>sqlite3 -version

查看python版本

> python3

- 如果python版本不是3.9.5，请执行一下命令

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

查看pip3 是否安装成功

> pip3 list

配置pip3从阿里云上下载

> vim ~/.pip/pip.conf

- 输入以下内容

> [global]
> index-url = http://mirrors.aliyun.com/pypi/simple/
> trusted-host = mirrors.aliyun.com

安装git

> yum install git

下载 GreaterWMS 从 gitee

> git clone https://gitee.com/Singosgu/GreaterWMS.git// 

提权 GreaterWMS 文件夹

> chmod -R 755 GreaterWMS

进入GreaterWMS文件夹

> cd GreaterWMS>pip3 install -r requirements.txt

- 有些时候，你安装这些库会出问题，是因为python3版本的问题，不用担心，pip3 install 出错的库就可以了.

> /usr/local/bin/daphne -p 8008 greaterwms.asgi:application
- 现在打开浏览器，输入"127.0.0.1:8008"，你会看到500错误，恭喜你，你已经可以正常部署接下来的事情了

回到GreaterWMS文件夹

> Ctrl + C

数据库生成

> python3 manage.py makemigrations // 数据库生成

数据库迁移

> python3 manage.py migrate // 数据库迁移

> /usr/local/bin/daphne -p 8008 greaterwms.asgi:application

- 现在打开浏览器，输入"127.0.0.1:8008"，你会看到项目已经运行了

输入 "127.0.0.1:8008/myip", 你会得到你的内网IP，一定记住它 

回到GreaterWMS文件夹

> Ctrl + C
> cd templates

等待Yarn安装完成，其实你也可以npm install ，就是会慢一点
更改yarn为国内源
> yarn config set registry https://registry.npm.taobao.org/
> /usr/local/bin/yarn install

使用quasar命令启动前端页面

> /usr/local/bin/quasar d

- 前端会向 "127.0.0.1:8008"发请求, 在这里我们只是看下项目是不是可以运行

退回到templates文件夹

> Ctrl + C // 退回到templates文件夹

- 从2.0.19版本以后，优化了请求地址修改方式，直接修改templates/dist/spa/statics/baseurl.js，中的baseurl和wsurl，就可以成功更改前端请求地址，不再需要做下面的quasar build打包工作。如果需要修改前端内容，则还需要修改templates/public/statics/baseurl.js中的baseurl和wsurl，然后重新使用quasar build进行打包，更改 "127.0.0.1" 成你的内网IP, baseurl 是http请求地址 , ws 是 websocket请求地址
- 按下 Esc 然后输入 ":wq" 去保存修改
- 现在，你已经知道怎么部署和修改请求地址了

需要对修改进行重新打包

> /usr/local/bin/quasar build

回到GreaterWMS文件夹

> cd ..
> /usr/local/bin/daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application

- 现在，打开浏览器，输入 "你的外网IP:8008"，你可以看到项目已经运行了