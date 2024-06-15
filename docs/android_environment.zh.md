# 安卓环境搭建

---
node版本要求
> node v14.19.3

app源码项目地址
> 下载地址: https://gitee.com/Singosgu/scanner

安装JDK1.8

> 下载地址：https://www.56yhz.com/media/windows/jdk-8u281-windows-x64.exe 

- 一直next即可

安装Cordova插件
- 项目目录下运行npm install -g cordova

安装AndRoid Studio软件

> 下载地址为：https://developer.android.google.cn/studio/

- 一直next,第一次运行，需要安装SDK,全部选是即可

> ![](https://www.56yhz.com/media/windows/1.jpeg)

- 打开Android Studio,点击右边的project——More Actions——SDK Manager——SDK Platforms,选中下边的Hide Obsolete Packages

> ![](https://www.56yhz.com/media/windows/2.jpeg)]
(切换到SDK-TOOLS)

- 切换到SDK-TOOLS,选中图中所示

> ![](https://www.56yhz.com/media/windows/3.jpeg)

- 再选中右方的Show Package Details，选中30版本的即可，点击Apply,等下载完成，再点确定

下载Gradle，下载完成后解压到其他路径即可

>下载路径为https://downloads.gradle-dn.com/distributions/gradle-4.10.3-all.zip

环境变量配置
创建系统环境变量JAVA_HOME:为JDK安装路径，默认路径即图中所示

> ![](https://img-blog.csdnimg.cn/3328a70f4a044fd6b82488363367919d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbTBfNjE0MzExNzU=,size_20,color_FFFFFF,t_70,g_se,x_16)

创建系统环境变量Gradle:为上一一步中gradle-4.10.3-all.zip解压后的路径

> ![](https://www.56yhz.com/media/windows/4.jpeg)

创建系统环境变量ANDROID_HOME和ANDROID_SDK_ROOT:为Android SDK的安装路径

> ![](https://www.56yhz.com/media/windows/5.jpeg)

编辑环境变量PATH，添加如图所示

![](https://www.56yhz.com/media/windows/6.jpeg)

验证安卓环境是否配置完成
输入 cordova requirements 检查环境，如果成功的话如下所示：

![](https://www.56yhz.com/media/windows/7.jpeg)

安装前端环境
> npm install -g npm
> npm config set registry https://registry.npm.taobao.org
> npm install -g yarn
> yarn config set registry https://registry.npm.taobao.org/
> npm install -g @quasar/cli
> npm install -g core-js

初始化环境

- 项目目录下执行yarn install

生成apk测试环境(手机上打开USB调试模式，并且连接到电脑上，选择文件模式或者U盘模式)

- 项目目录下执行quasar d -m cordova -T android

> ![](https://www.56yhz.com/media/windows/9.jpeg)