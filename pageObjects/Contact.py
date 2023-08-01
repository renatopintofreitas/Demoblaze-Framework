from selenium.webdriver.common.by import By


class Contact:
    
    def __init__(self, driver):
        self.driver = driver
        
    contactLink = (By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a")
    contactEmailField = (By.ID, "recipient-email") 
    contactNameField = (By.ID, "recipient-name")
    contactMsgField = (By.ID, "message-text")   
    contactSendMsgButton = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]")
    contactCloseButton = (By.XPATH, "/html/body/div[1]/div/div/div[3]/button[1]")
    
    
    def gotoContact(self):
        return self.driver.find_element(*Contact.contactLink)  
    
    def typeContactEmail(self):
        return self.driver.find_element(*Contact.contactEmailField)
    
    def typeContactName(self):
        return self.driver.find_element(*Contact.contactNameField)
        
    def typeContactMsg(self):
        return self.driver.find_element(*Contact.contactMsgField)    
    
    def gotoContactSendMsg(self):
        return self.driver.find_element(*Contact.contactSendMsgButton)
        
    def gotoCloseContact(self):
        return self.driver.find_element(*Contact.contactCloseButton)