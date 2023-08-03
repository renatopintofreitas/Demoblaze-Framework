from selenium.webdriver.common.by import By



class HomePage:
    
    def __init__(self, driver):
        self.driver = driver
        
        
    loginLink = (By.ID, "login2")
    userField = (By.ID, "loginusername")
    passwordField = (By.ID, "loginpassword")
    loginButton = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
    signupLink = (By.ID, "signin2")
    userFieldSignup = (By.ID, "sign-username")
    passwordFieldSignup = (By.ID, "sign-password")
    signupButton = (By.XPATH, "/html/body/div[2]/div/div/div[3]/button[2]")
    signupCloseButton = (By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]")
    productCards = (By.XPATH, "//div[@class='card h-100']")
    
    
    
    def gotoSignup(self):
        return self.driver.find_element(*HomePage.signupLink)
    
    def typeUsernameSignup(self):
        return self.driver.find_element(*HomePage.userFieldSignup)
    
    def typePasswordSignup(self):
        return self.driver.find_element(*HomePage.passwordFieldSignup)
    
    def clickSignupButton(self):
        return self.driver.find_element(*HomePage.signupButton)
    
    def clickSignupClose(self):
        return self.driver.find_element(*HomePage.signupCloseButton)
    
    def gotoLogin(self):
        return self.driver.find_element(*HomePage.loginLink)
    
    def typeUsername(self):
        return self.driver.find_element(*HomePage.userField)
    
    def typePassword(self):
        return self.driver.find_element(*HomePage.passwordField)
    
    def clickLoginButton(self):
        return self.driver.find_element(*HomePage.loginButton)