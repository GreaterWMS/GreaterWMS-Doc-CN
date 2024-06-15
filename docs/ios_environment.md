# IOS environment construction

---

Download Xcode

> The latest version is Xocde Beta 13.2,

> https://download.developer.apple.com/Developer_Tools/Xcode_13.2_beta/Xcode_13.2_beta.xip

- Rename the decompressed and successfully installed application to Xcode.app and copy it to the /Application directory

Download plugin

> Go to src-cordovan under templates in the project directory and execute:

Check the current environment

> cordova requirements

> ![image-20211030133647439](https://tva1.sinaimg.cn/large/008i3skNgy1gvxa4fk0j2j30ss05ymyc.jpg)

Install ios-deploy

> brew install ios-deploy

Install CocoaPods

> sudo gem install cocoapods

Packaging the IOS client

- Deploy ios client

In the templates/src-cordova directory

> cordova platform ios

> ![image-20211030125105616](https://tva1.sinaimg.cn/large/008i3skNly1gvx93uks9hj30uq074acb.jpg) Open the ios directory of the project with Xcode, such as templates/src-cordova/platforms/ios, and add the Apple developer account Apple ID (the developer account needs to be registered by yourself) to register your own test device on the Apple developer website https://developer.apple.com/account/resources/devices/list

> ![image-20211030151000631](https://tva1.sinaimg.cn/large/008i3skNgy1gvxctgrhl1j31tm0kqmzy.jpg)

- Note: The device added here refers to the tested Apple mobile phone. The mac will be automatically added by the system after binding the device using xcode. The binding device needs to know the UDID of its own device in advance to obtain the UDID method: http://www.pgyer. com/tools/udid You can use WeChat to scan the code, and then open it with the built-in Safari browser to get the UDID. Click Xcode—Preferences—Accounts to add an Apple ID

![](/media/editor/008i3skNgy1gvxbxswiypj319k0t8tb8_20220605111748890119.jpeg)

- If the Team in this interface does not have a certificate at this time, you can click the Download Manual Profile below to download

Project developer certificate download

> ![image-20211030145757012](https://tva1.sinaimg.cn/large/008i3skNgy1gvxcgxz5prj31o80ig0xa.jpg) Select the developer certificate we just downloaded at the Team in the project, and the Signing Certificate select the similar certificate of Apple Development

Officially packaged, after the above preparations are ready, enter Xcode, Devices and select our test device

> ![image-20211030153050463](https://tva1.sinaimg.cn/large/008i3skNgy1gvxdf73lh6j31oq07iwgk.jpg)

After everything is set up, there is a button similar to play above Xcode, click on it, you can complete the IOS installation package into the current test iPhone

> ![image-20211030153439683](https://tva1.sinaimg.cn/large/008i3skNgy1gvxdj59ud8j315f0u0jvi.jpg)

- Note: When the terminal displays the following information, it means that the IOS application is already running on the iPhone: **2021-10-30 10:02:31.694411+0800 GreaterWMS--Open Source Warehouse Management System[436:12140] [Snapshotting] Snapshotting a view (0x10702d600, UIKeyboardImpl) that has not been rendered at least once requires afterScreenUpdates:YES.**Also shows "Finshed running XXXXXX on device name" above Xcode

> ![image-20211030154017111](https://tva1.sinaimg.cn/large/e6c9d24egy1h199fqxjw4j20u01sx0u4.jpg)