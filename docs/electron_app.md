# Electron Apps

---
test run，Go to templates in the GreaterWMS project directory and open cmd
> execute yarn install
>quasar d -m electron

Build,Go to templates in the GreaterWMS project directory and open cmd

> execute yarn install
> execute quasar build -m electron -P always

- After the packaging is completed, an installation file will be generated under the GreaterWMS project directory \template\dist\electron\Packaged\
- exe under windows, dmg under mac, just click to install.

 If it is the first time to run this packaging command, he will download many dependent packages, some of which are too large and not easy to download. In order to solve this problem, we made an electron dependent package, which the user downloads and decompresses. Go to C:\Users\{your username}\AppData\Local\

> The download address of electron.zip is: [https://data.56yhz.com/media/windows/electron.zip](https://data.56yhz.com/media/windows/electron.zip)

Then run yarn install and quasar build -m electron -P always in turn

> Success!