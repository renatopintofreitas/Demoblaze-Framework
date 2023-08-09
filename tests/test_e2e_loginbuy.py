from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time        
        
        
from pageObjects.Cart import Cart
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.e2eData import e2eData
        
        
        
class Test_e2e(BaseClass):
    
    def test_e2e_loginbuy(self, getData):
            
        log = self.getLogger()
        
        clickLogin = HomePage(self.driver)
        clickLogin.gotoLogin().click()
        
        self.wait_for_loginform()

        writeUser = HomePage(self.driver)
        writeUser.typeUsername().send_keys(getData["email"])

        writePassword = HomePage(self.driver)
        writePassword.typePassword().send_keys(getData["password"])

        clickLoginBox = HomePage(self.driver)
        clickLoginBox.clickLoginButton().click()

        userWelcome = self.driver.find_element(By.ID, "nameofuser")
        if userWelcome is not None:
            print("Login Successful")
        else:
            print("Login Failed")        

        #time.sleep(2)    
          
        
        productCards = Cart(self.driver)
        products = productCards.getProductCards()
        
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == getData["product"]:
                log.info(productName)
                product.find_element(By.XPATH, "div/h4/a").click()
                time.sleep(1)
                break
                
                
        addToCart = Cart(self.driver)
        addToCart.putInCart().click()
        
        alert = self.wait_for_alert()
        alertText = alert.text
        log.info(alertText)
        alert.dismiss()
                
        clickCart = Cart(self.driver)
        clickCart.gotoCart().click()        

        productprice = clickCart.getProductPrice().text
        totalprice = clickCart.getTotalToPay().text

        assert productprice == totalprice, "The price does not match the total price."
        log.info("Total is: "+totalprice)

        placeOrder = Cart(self.driver)
        placeOrder.clickPlaceOrder().click()
        
        writeCustomerName = Cart(self.driver)
        writeCustomerName.typeCustomerName().send_keys(getData["name"])
        
        writeCustomerCountry = Cart(self.driver)
        writeCustomerCountry.typeCustomerCountry().send_keys(getData["country"])
        
        writeCustomerCity = Cart(self.driver)
        writeCustomerCity.typeCustomerCity().send_keys(getData["city"])
        
        writeCustomerCC = Cart(self.driver)
        writeCustomerCC.typeCustomerCC().send_keys(getData["creditcard"])
        
        writeCustomerMonth = Cart(self.driver)
        writeCustomerMonth.typeCustomerMonth().send_keys(getData["month"])
        
        writeCustomerYear = Cart(self.driver)
        writeCustomerYear.typeCustomerYear().send_keys(getData["year"])
        
        clickOrderPurchase = Cart(self.driver)
        clickOrderPurchase.clickPurchase().click()
        

        buymsg = clickOrderPurchase.sayPurchaseSuccess().text

        assert "Thank you for your purchase!" in buymsg
        log.info(buymsg)

        #driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button").click()
        time.sleep(3)
        
    @pytest.fixture(params=e2eData.test_e2e_data)
    def getData(self, request):
        return request.param