from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

from pageObjects.Contact import Contact
from utilities.BaseClass import BaseClass
from testData.contactData import ContactData


class TestContact(BaseClass):
    
    def test_contactMessage(self, getData):
        
        log = self.getLogger()
        clickContact = Contact(self.driver)
        clickContact.gotoContact().click()
        
        writeContactEmail = Contact(self.driver)
        writeContactEmail.typeContactEmail().send_keys(getData["email"])
        
        writeContactName = Contact(self.driver)
        writeContactName.typeContactName().send_keys(getData["name"])
        
        writeContactMsg = Contact(self.driver)
        writeContactMsg.typeContactMsg().send_keys(getData["message"])
        time.sleep(3)
        
        clickContactSendMsg = Contact(self.driver)
        clickContactSendMsg.gotoContactSendMsg().click()
        
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        
        alert = self.driver.switch_to.alert
        alertText = alert.text
        print(alertText)
        alert.dismiss()
        time.sleep(3)
        #clickContactClose = Contact(self.driver)
        #clickContactClose.gotoCloseContact().click()
        
        log.info("alert message was: " +alertText)
        
        time.sleep(3)
        self.driver.refresh()
        
    @pytest.fixture(params=ContactData.test_Contact_data)
    def getData(self, request):
        return request.param