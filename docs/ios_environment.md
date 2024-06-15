# IOS 环境搭建

---

下载Xcode 

​		目前最新版本为Xocde Beta 13.2，下载地址为：https://download.developer.apple.com/Developer_Tools/Xcode_13.2_beta/Xcode_13.2_beta.xip

```
#将解压出来并安装成功后的应用改名为Xcode.app复制到/Application目录下
 mv Xcode.app /Users/{你的mac机器用户名}/Applications
```

二，下载插件

​		进入项目目录下的templates下的src-cordovan，执行：

```
##检测当下环境
cordova requirements
```

![image-20211030133647439](https://tva1.sinaimg.cn/large/008i3skNgy1gvxa4fk0j2j30ss05ymyc.jpg)

```
#安装ios-deploy
brew install ios-deploy
#安装CocoaPods
sudo gem install cocoapods
```

三，打包IOS客户端

1.

```
#部署ios客户端
cordova platform ios
```

![image-20211030125105616](https://tva1.sinaimg.cn/large/008i3skNly1gvx93uks9hj30uq074acb.jpg)

用Xcode打开项目的ios目录,比如templates/src-cordova/platforms/ios，并添加苹果开发者账号的Apple ID(开发者账号需要自己注册)

2. 在苹果开发者网站上注册自己的测试设备

   https://developer.apple.com/account/resources/devices/list

   ![image-20211030151000631](https://tva1.sinaimg.cn/large/008i3skNgy1gvxctgrhl1j31tm0kqmzy.jpg)

注意：这里添加的设备是指测试的苹果手机，mac会在使用xcode绑定设备以后系统自动添加，绑定设备需要提前知晓自己设备的UDID

获得UDID的方法：

​	  http://www.pgyer.com/tools/udid

​		可利用微信扫码，然后用内置的Safari 浏览器打开即可获得UDID

3. 点击Xcode—Preferences—Accounts，添加Apple ID

![image-20211030143927297](https://tva1.sinaimg.cn/large/008i3skNgy1gvxbxswiypj319k0t8tb8.jpg) 

如果此时这个界面的Team 没有证书，可以点击 下面的Download Manual Profile进行下载

4.项目开发者证书下载

![image-20211030145757012](https://tva1.sinaimg.cn/large/008i3skNgy1gvxcgxz5prj31o80ig0xa.jpg)

在项目里的Team处选择我们刚刚下载的开发者证书，Signing Certificate 选择Apple Development的类似证书

5.正式打包，以上准备工作都就绪后，进入Xcode,Devices处选择我们的测试设备

![image-20211030153050463](https://tva1.sinaimg.cn/large/008i3skNgy1gvxdf73lh6j31oq07iwgk.jpg)

6.一切设置好以后，在Xcode上方有一个类似播放的按钮，点击他，即可完成将IOS安装包打入当前的测试苹果手机中

![image-20211030153439683](https://tva1.sinaimg.cn/large/008i3skNgy1gvxdj59ud8j315f0u0jvi.jpg)

注：当终端显示以下信息，就表示IOS应用已在苹果手机上运行：

**2021-10-30 10:02:31.694411+0800 GreaterWMS--Open Source Warehouse Management System[436:12140] [Snapshotting] Snapshotting a view (0x10702d600, UIKeyboardImpl) that has not been rendered at least once requires afterScreenUpdates:YES.**

在Xcode上方也会显示“Finshed runing XXXXXX on 设备名称”

​	苹果手机运行效果图

![](https://tva1.sinaimg.cn/large/e6c9d24egy1h199fqxjw4j20u01sx0u4.jpg)