Docker下使用GreaterWMS（本文档适用于具备Docker基础的用户使用）

1.安装或升级Docker客户端
    curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
    //如果提示没有curl再执行sudo apt install curl 或 yum -y install curl


2.配置加速器（国内） ##国内加速，全球用户则不需要配加速器
    sudo mkdir -p /etc/docker
    sudo vim /etc/docker/daemon.json 
    {
      "registry-mirrors": ["https://w61q8mf4.mirror.aliyuncs.com"]
    }
    sudo systemctl daemon-reload
    sudo systemctl enable docker
    sudo systemctl restart docker

3.安装Docker-compose
    curl -L https://github.com/docker/compose/releases/download/1.29.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

4.本机试用（试运行）
    

	   docker run -itd --name greaterwms_v2.1.18 -p 8008:8008 -d greaterwms/greaterwms:v2.1.18
    

5.安装git
    //Ubuntu下安装git
    apt-get install git
    //CentOS下安装git
    yum install git

6.开始部署
    //拉取代码
    git clone https://gitee.com/Singosgu/GreaterWMS.git
    //运行项目前需要修改baseurl.js的内容
    vim templates/public/statics/baseurl.js //将127.0.0.1修改为服务器的IP地址
    //运行项目前需要修改nginx.conf的内容
    vim nginx.conf //将127.0.0.1修改为本机IP地址，如果部署到服务器，修改为服务器IP地址
	//启动项目
    docker-compose up -d
    //特别备注：执行docker-compose up -d后会自动下载前端依赖，有时会下载失败，导致前端无法启动，此时先执行docker-compose down再docker-compose up -d重新下载，直至成功为止。
	//特别备注：用户也可以在settings.py中改成mysql，具体配置可自行研究

7.发布前端代码
//进入前端容器
docker exec -it greaterwms_front_v2.1.18 /bin/bash
//容器内进入templates目录
cd templates
//编译前端代码
quasar build 

8. 查看supervisord访问日志

   tail -f greaterwms_server_access.log 

   ![image-20220129221112110](https://tva1.sinaimg.cn/large/008i3skNgy1gyuwdrrqzrj30ky0b4djp.jpg)

9. 访问入口

```
前端：http://127.0.0.1:8080 或者 http://服务器IP:8080

后端：http://127.0.0.1:8008 或者 http://服务器IP:8008

nginx: http://127.0.0.1 或者http://服务器IP