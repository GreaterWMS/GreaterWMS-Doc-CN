# Android Apk 签名

---

生成apk文件

> 项目下的templates目录下执行quasar build -m android

- 执行完成以后会在/GreaterWMS项目目录/templates/dist/cordova/android/apk/release/生成一个未签名的文件

- release处打开一个终端,预备生成签名文件,按提示输入密码，输入信息时一路回车，在最后一步生成国家/地区时输入CN,并Y确认NN

> 输入keytool -genkey -v -keystore greaterwms.keystore -alias Greaterwms -keyalg RSA -keysize 2048 -validity 20000

- greaterwms.keystore为生成的签名文件，Greaterwms为别名

> ![](https://data.56yhz.com/media/windows/10.jpeg)

开始签名

> jarsigner -verbose -keystore greaterwms.keystore -signedjar Greaterwms.apk app-release-unsigned.apk Greaterwms

- greaterwms.keystore为上一步我们生成的签名文件 
- Greaterwms.apk为要生成的已签名的文件 
- app-release-unsigned.apk为之前打包时生成的未签名的文件

> ![](https://data.56yhz.com/media/windows/11.jpeg)

安装已签名的apk文件

> 输入adb install Greaterwms.apk

> ![](https://data.56yhz.com/media/windows/13.jpeg)