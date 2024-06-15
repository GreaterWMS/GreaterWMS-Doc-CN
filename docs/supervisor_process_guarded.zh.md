# Supervisor 守护进程

---

### CentOS配置

> yum install epel-release
> yum install -y supervisor
> pip3 install supervisor
> systemctl enable supervisord //设置开机自启
> systemctl start supervisord  //启动supervisord服务
> systemctl restart supervisord //重复supervisord服务
> vim /etc/supervisord.conf //修改supervisord配置文件,加入以下内容

```shell
[program:greaterwms]
directory=/GreaterWMS/  ; GreaterWMS代码目录
user=root
command=daphne -b 0.0.0.0 -p 8008 greaterwms.asgi:application
autostart=true
autorestart=true
startsecs=0
stopwaitsecs=0
stdout_logfile=/GreaterWMS/greaterwms_server_access.log
stderr_logfile=/GreaterWMS/greaterwms_server_err.log
redirect_stderr=true
[include]
files = /etc/supervisor/conf.d/*.conf
```

其他常用命令

>supervisorctl reload  //读取有更新（增加）的配置文件，不会启动新添加的程序
>supervisorctl update //重启配置文件修改过的程序
>supervisorctl status  //查看状态

### Ubuntu配置

> apt-get update
> apt-get install supervisor -y
> pip3 install supervisor
> 生成supervisord配置文件的方式参考CentOS