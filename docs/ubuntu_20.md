# Ubuntu 20 64位 部署

---

> sudo apt update
> sudo apt upgrade

安装 vim

> sudo apt install vim

进入Home目录

> cd ~

把 "alias vi=vim" 加进 bashrc

>vim .bashrc

刷新生效bashrc

>source .bashrc

安装git

>sudo apt install git

下载 GreaterWMS 从 gihub

>sudo git clone https://gitee.com/Singosgu/GreaterWMS.git

安装nodejs

>wget https://nodejs.org/dist/v14.18.3/node-v14.18.3-linux-x64.tar.gz
> tar zvxf node-v14.18.3-linux-x64.tar.gz -C /usr/local
> echo ''' export NODE_HOME=/usr/local/node-v14.18.3-linux-x64 export PATH=$PATH:$NODE_HOME/bin export NODE_PATH=$NODE_HOME/lib/node_modules''' /etc/profile

使环境变量立即生效

>source /etc/profile 
>sudo ln -sf /usr/local/node-v14.18.3-linux-x64/bin/node /usr/bin/node
>sudo ln -s /usr/local/node-v14.18.3-linux-x64/bin/npm /usr/bin/npm

验证node是否安装成功

>sudo node -v

验证npm是否安装成功

>sudo npm -v

- 这步完成以后，你需要重新启动你的Terminal，要不然升级不生效

> sudo npm install npm -g
> sudo npm install yarn -g
> sudo npm install -g @quasar/cli

确定你的python版本是3.8以上版本，原则上3.6也是可以的，但是安装库会有些问题

> python3

确定你是否安装有 pip3

> pip3 list

如果你没有pip3 ，就安装一下

> sudo apt install python3-pip

检查下是否安装成功

> pip3 list

提权 GreaterWMS 文件夹

>sudo chmod -R 755 GreaterWMS

> cd GreaterWMS
> sudo pip3 install -r requirements.txt

有些时候，你安装这些库会出问题，是因为python3版本的问题，不用担心，sudo pip3 install 出错的库就可以了.

> sudo daphne -p 8008 greaterwms.asgi:application
> 现在打开浏览器，输入"127.0.0.1:8008"，你会看到500错误，恭喜你，你已经可以正常部署接下来的事情了

回到GreaterWMS文件夹

> Ctrl + C

数据库生成和迁移

> sudo python3 manage.py makemigrations
> sudo python3 manage.py migrate

启动GreaterWMS

> sudo daphne -p 8008 greaterwms.asgi:application
- 现在打开浏览器，输入"127.0.0.1:8008"，你会看到项目已经运行了
- 输入 "127.0.0.1:8008/myip", 你会得到你的内网IP，一定记住它 

回到GreaterWMS文件夹

> Ctrl + C

进入 templates 文件夹

> cd templates

更改yarn为国内源

> sudo yarn config set registry https://registry.npm.taobao.org/

等待Yarn安装完成，其实你也可以sudo npm install ，就是会慢一点

> sudo yarn install

使用quasar命令启动前端页面

> sudo quasar d

- 前端会向 "127.0.0.1:8008"发请求, 在这里我们只是看下项目是不是可以运行

- 从2.0.19版本以后，优化了请求地址修改方式，直接修改templates/dist/spa/statics/baseurl.js，中的baseurl和wsurl，就可以成功更改前端请求地址，不再需要做下面的quasar build打包工作。
- 如果需要修改前端内容，则还需要修改templates/public/statics/baseurl.js中的baseurl和wsurl，然后重新使用quasar build进行打包

>按下 Esc 然后输入 ":wq" 去保存修改
>现在，你已经知道怎么部署和修改请求地址了

需要对修改进行重新打包

> sudo quasar build

回到GreaterWMS文件夹

> cd ..

重新启动GreaterWMS

> sudo daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application

- 现在，打开浏览器，输入"内网IP:8008"