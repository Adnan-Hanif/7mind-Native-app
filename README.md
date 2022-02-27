# 7mind-Native-app

Hello! There are some important steps for automating a native app first of all connecting a real andriod or ios phone with laptop ( use a good quality USB cable) Enable the developing mode in your cell phone after 7 to 10 time clicking on build number option which you will find in about phone option of setting and On the USB Debugging. Follow the following steps step 1 : Download SDK tools

https://developer.android.com/studio
Step 2 : Unzip folder & Extract platform tools Step 3 : Set environment variables

ANDROID_HOME = location of sdk folder
Path : append path of platform_tools folder
Step 4 : Check command adb devices on command line Step 5 : Make device ready ( Enabing USB Debugging in developing mode) Step 6 : Connect device to computer system thorugh USB cable Step 7 : Run command adb devices

adb stands for android debug bridge
you will find the id of your device in CMD. In my case the id of my device is bc6aa0a5.
After connecting device with laptop succesfully Download the following software Step 1 : installation of Python Step 2 : Set Environment Veriables Setp 3 : Check the version of python and pip in CMD with the help of -version comamand Step 4 : Installation of Pycharm Step 5 : Installation of Appium Desktop

https://github.com/appium/appium-desktop/releases/tag/v1.22.2
On the appium server and then click on Start Inspecition Session Set the desired Abilities (in my Case) or you can with it in pycharm { "platformName": "Android", "deviceName": "SM G901F", "udid": "bc6aa0a5", "app": "C:\Users\Mirza Adnan Hanif\Desktop\7Mind Meditation reinvented_v2.55.0_apkpure.com.apk" }

7Mind application will download in the Android Device.

Open Pycharm and install the following package

Appium python client go to file > Setting > + > write appium python client and install.

Then make a new file with any name Then you can paste the following code or you can clone the project.

from appium import webdriver from selenium.webdriver import Keys

desiredapp = { "platformName": "Android", "deviceName": "SM G901F", "udid": "bc6aa0a5", "app": "C:\Users\Mirza Adnan Hanif\Desktop\7Mind Meditation reinvented_v2.55.0_apkpure.com.apk" }

driver = webdriver.Remote("http://localhost:4723", desiredapp)

driver..find_element_by_link_text('Continue').click()

driver.find_element_by_Id("de.sevenmind.android:id/actionButton").click()

Email = driver.find_element_by_Id("de.sevenmind.android:id/actionButton") Email.find_element_by_link_text('Email').click()

emailInput = driver.find_element_by_Id("de.sevenmind.android:id/cellDialogTextInputEditText") emailInput.send.keys("aadi@gmail.com").sendKeys(Keys.ENTER)

passwordInput = driver.find_element_by_Id("de.sevenmind.android:id/cellDialogTextInputEditText") passwordInput.send.keys("qwerty").sendKeys(Keys.ENTER) driver.find_element_by_Id("de.sevenmind.android:id/actionButton").click()
