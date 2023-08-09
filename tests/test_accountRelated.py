from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from pageObjects.HomePage import HomePage

from utilities.BaseClass import BaseClass
#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
         
    def test_signup(self):
        
        
        clickSignup = HomePage(self.driver)
        clickSignup.gotoSignup().click()
        
        time.sleep(1)
        
        writeUserSignup = HomePage(self.driver)
        writeUserSignup.typeUsernameSignup().send_keys("renato8@nether.com")
        
        writePasswordSignup = HomePage(self.driver)
        writePasswordSignup.typePasswordSignup().send_keys("abcabc")
        
        clickSignupBox = HomePage(self.driver)
        clickSignupBox.clickSignupButton().click()
        
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        
        alert = self.driver.switch_to.alert
        alertText = alert.text
        
        if alertText == "This user already exist.":
            print(alertText)
            alert.dismiss()
            time.sleep(1)
            closeSignupBox = HomePage(self.driver)
            closeSignupBox.clickSignupClose().click()
            
        else:
            print(alertText)
            alert.accept()
            
        
    def test_login(self):
        
        clickLogin = HomePage(self.driver)
        clickLogin.gotoLogin().click()
        
        time.sleep(1)

        writeUser = HomePage(self.driver)
        writeUser.typeUsername().send_keys("renato8@nether.com")

        writePassword = HomePage(self.driver)
        writePassword.typePassword().send_keys("abcabc")

        clickLoginBox = HomePage(self.driver)
        clickLoginBox.clickLoginButton().click()

        userWelcome = self.driver.find_element(By.ID, "nameofuser")
        if userWelcome is not None:
            print("Login Successful")
        else:
            print("Login Failed")        

        time.sleep(5)    