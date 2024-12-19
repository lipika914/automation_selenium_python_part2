from POM.BaseClass import BasePage
import time
class LoginPage(BasePage):
  def __init__(self, driver):
   super().__init__(driver)
   self.url = "https://rahulshettyacademy.com/loginpagePractise/"
  def open(self):
   self.driver.get(self.url)
  def login(self, username, password):
    self.wait_for_element("id", "username").send_keys(username)
    self.wait_for_element("id", "password").send_keys(password)
    self.wait_for_element("id", "signInBtn").click()
    time.sleep(20)

 
