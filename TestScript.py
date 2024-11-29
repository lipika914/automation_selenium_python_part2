from selenium import webdriver
from POM.LoginClass import LoginPage
# Step 1: Setup WebDriver
driver = webdriver.Chrome()

login_page = LoginPage(driver)
login_page.open()
login_page.login("rahulshettyacademy", "learning")
# Step 3: Quit the browser
login_page.quit()