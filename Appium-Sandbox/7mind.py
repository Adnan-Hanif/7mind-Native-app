from appium import webdriver
from selenium.webdriver import Keys

desiredapp = {
  "platformName": "Android",
   "deviceName": "SM G901F",
  "udid": "bc6aa0a5", 
  "app": "C:\\Users\\Mirza Adnan Hanif\Desktop\\7Mind Meditation reinvented_v2.55.0_apkpure.com.apk"
}

driver = webdriver.Remote("http://localhost:4723", desiredapp)

driver..find_element_by_link_text('Continue').click()

driver.find_element_by_Id("de.sevenmind.android:id/actionButton").click()

Email = driver.find_element_by_Id("de.sevenmind.android:id/actionButton")
Email.find_element_by_link_text('Email').click()

emailInput = driver.find_element_by_Id("de.sevenmind.android:id/cellDialogTextInputEditText")
emailInput.send.keys("aadi@gmail.com").sendKeys(Keys.ENTER)

passwordInput = driver.find_element_by_Id("de.sevenmind.android:id/cellDialogTextInputEditText")
passwordInput.send.keys("qwerty").sendKeys(Keys.ENTER)
driver.find_element_by_Id("de.sevenmind.android:id/actionButton").click()



