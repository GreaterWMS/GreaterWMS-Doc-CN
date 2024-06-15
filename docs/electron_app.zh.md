# Electron 应用

---
试运行，进入GreaterWMS项目目录下的templates下，打开cmd
> 执行yarn install
> 执行quasar d -m electron

打包，进入GreaterWMS项目目录下的templates下，打开cmd

> 执行yarn install
> 执行quasar build -m electron -P always

- 打包完成以后会在GreaterWMS项目目录\template\dist\electron\Packaged\下生成一个安装文件
- windows下面是exe,mac下面是dmg，直接点击安装即可。

 如果是第一次运行这个打包命令，他会去下载很多依赖包，有些依赖包很大，不容易下载，为了解决这个问题，我们制作了一个electron依赖包，用户下载下来，解压到C:\Users\{你的用户名}\AppData\Local\下即可

> electron.zip下载地址为： [https://data.56yhz.com/media/windows/electron.zip](https://data.56yhz.com/media/windows/electron.zip)

然后再依次运行yarn install和quasar build -m electron -P always

> 成功！