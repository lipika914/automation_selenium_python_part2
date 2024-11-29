# Page Object Model (POM) Framework for Test Automation  

This repository demonstrates the **Page Object Model (POM)** design pattern for creating scalable and maintainable test automation scripts using Python and Selenium.

---

##  Directory Structure  

The project is structured for clarity and easy navigation:  

```
.
├── POM/                     # Contains Page Object Model classes
│   ├── BaseClass.py         # Base class with common methods (e.g., setup, quit)
│   ├── LoginClass.py        # Login page class with locators and methods
│   
├── TestScript.py            # Contains test scripts
├── README.md                # Project documentation


---

## 📝 Overview  

### What is Page Object Model (POM)?  
The **Page Object Model** is a design pattern for test automation frameworks where:  
1. Each **page** or **component** of a web application is represented as a **class**.  
2. All locators and actions for that page are defined in that class.  
3. Tests interact with these page classes rather than directly accessing locators.

## 🔧 Setup and Installation  

### Prerequisites  
- Python 3.7 or higher  
- Browser WebDriver (e.g., ChromeDriver for Google Chrome)  

### Installation Steps  
1. Clone the repository:  
   ```bash
 (https://github.com/lipika914/automation_selenium_python_part2)
   ```   

2. Ensure the appropriate WebDriver is installed and added to system’s PATH.  

---

## Usage  

### Running a Test Script  
 Run a test script using Testscript.py    

### Adding a New Page  
1. Create a new Python file in the `POM` folder .  
2. Define a class for the page. Include locators and methods for all actions related to the page.  
3. Use the page class in your test scripts for interactions.  

---

## Example Code  

### **BaseClass.py**  
Handles common functionalities like browser setup and teardown:  
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def quit(self):
        self.driver.quit()
```
### **LoginClass.py**  
Represents the login page, encapsulating its locators and actions:  
```python
from POM.BaseClass import BasePage
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
```

### **TestScript.py**  
A test script using the POM classes:  
```python
from selenium import webdriver
from POM.LoginClass import LoginPage
# Step 1: Setup WebDriver
driver = webdriver.Chrome()

login_page = LoginPage(driver)
login_page.open()
login_page.login("rahulshettyacademy", "learning")

# Step 3: Quit the browser
login_page.quit()
```


