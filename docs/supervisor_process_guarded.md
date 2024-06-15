# Supervisor daemon

---

### CentOS configuration

> yum install epel-release
> yum install -y supervisor
> pip3 install supervisor
> systemctl enable supervisord //Set the boot to start automatically
> systemctl start supervisord //Start supervisord service
> systemctl restart supervisord //duplicate supervisord service
> vim /etc/supervisord.conf //Modify the supervisord configuration file and add the following

```shell
[program:greaterwms]
directory=/GreaterWMS/ ; GreaterWMS code directory
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
````

Other common commands

>supervisorctl reload //Read the updated (increased) configuration file, will not start the newly added program
>supervisorctl update //Restart the program modified by the configuration file
>supervisorctl status //View status

### Ubuntu Configuration

> apt-get update
> apt-get install supervisor -y
> pip3 install supervisor
> Refer to CentOS for how to generate supervisord configuration files