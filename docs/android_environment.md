# Android environment construction

---

Install JDK1.8

> Download address: https://data.56yhz.com/media/windows/jdk-8u281-windows-x64.exe

- Just keep on next

Install the AndRoid Studio software

> The download address is: https://developer.android.google.cn/studio/

- Always next, the first time you run it, you need to install the SDK, you can choose all

> ![](https://data.56yhz.com/media/windows/1.jpeg)](https://data.56yhz.com/media/windows/1.jpeg)

- Open Android Studio, click project on the right - More Actions - SDK Manager - SDK Platforms, select Hide Obsolete Packages below

> ![](https://data.56yhz.com/media/windows/2.jpeg)](Switch to SDK-TOOLS)

- Switch to SDK-TOOLS, select the one shown in the picture


> ![](https://data.56yhz.com/media/windows/3.jpeg)

- Then select Show Package Details on the right, select version 30, click Apply, wait for the download to complete, and then click OK

Download Gradle, and unzip it to another path after the download is complete

> The download path is https://downloads.gradle-dn.com/distributions/gradle-4.10.3-all.zip

Environment variable configuration
Create a system environment variable JAVA_HOME: the JDK installation path, the default path is as shown in the figure

> ![](https://img-blog.csdnimg.cn/3328a70f4a044fd6b82488363367919d.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAbTBfNjE0MzExNzU=,size_70,FF_se,color_FF)

Create a system environment variable Gradle: the unzipped path of gradle-4.10.3-all.zip in the previous step


> ![](https://data.56yhz.com/media/windows/4.jpeg)

Create system environment variables ANDROID_HOME and ANDROID_SDK_ROOT: for the installation path of the Android SDK

> ![](https://data.56yhz.com/media/windows/5.jpeg)

Edit the environment variable PATH and add as shown

![](https://data.56yhz.com/media/windows/6.jpeg)

Verify that the Android environment is configured
Check the environment by typing cordova requirements, if successful as follows:

![](https://data.56yhz.com/media/windows/7.jpeg)

Generate apk test environment (open USB debugging mode on mobile phone, connect to computer, select file mode or U disk mode)

- Execute quasar d -m cordova -T android in the templates directory under the project

> ![](https://data.56yhz.com/media/windows/9.jpeg)