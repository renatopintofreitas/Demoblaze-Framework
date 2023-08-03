from selenium.webdriver.common.by import By



class Cart:
    
    def __init__(self, driver):
        self.driver = driver
        
        
    productCards = (By.XPATH, "//div[@class='card h-100']")
    productNameElem = (By.XPATH, "div/h4/a")
    addToCartButton = (By.LINK_TEXT, "Add to cart")
    gotoCartButton = (By.ID, "cartur")
    productPriceCart = (By.XPATH, "/html/body/div[6]/div/div[1]/div/table/tbody/tr/td[3]")
    totalToPayCart = (By.ID, "totalp")
    placeOrderButton = (By.XPATH, "/html/body/div[6]/div/div[2]/button")
    orderCustomerName = (By.ID, "name")
    orderCustomerCountry = (By.ID, "country")
    orderCustomerCity = (By.ID, "city")
    orderCustomerCC = (By.ID, "card")
    orderCustomerMonth = (By.ID, "month")
    orderCustomerYear = (By.ID, "year")
    orderPurchaseButton = (By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
    orderSuccessPurchase = (By.XPATH, "/html/body/div[10]/h2")
    
    
    
    def getProductCards(self):
        return self.driver.find_elements(*Cart.productCards)
    
    def getProductNames(self):
        return self.driver.find_elements(*Cart.productNameElem)
    
    def putInCart(self):
        return self.driver.find_element(*Cart.addToCartButton)
    
    def gotoCart(self):
        return self.driver.find_element(*Cart.gotoCartButton)
    
    def getProductPrice(self):
        return self.driver.find_element(*Cart.productPriceCart)
    
    def getTotalToPay(self):
        return self.driver.find_element(*Cart.totalToPayCart)
    
    def clickPlaceOrder(self):
        return self.driver.find_element(*Cart.placeOrderButton)
    
    def typeCustomerName(self):
        return self.driver.find_element(*Cart.orderCustomerName)
    
    def typeCustomerCountry(self):
        return self.driver.find_element(*Cart.orderCustomerCountry)
    
    def typeCustomerCity(self):
        return self.driver.find_element(*Cart.orderCustomerCity)
    
    def typeCustomerCC(self):
        return self.driver.find_element(*Cart.orderCustomerCC)
    
    def typeCustomerMonth(self):
        return self.driver.find_element(*Cart.orderCustomerMonth)
    
    def typeCustomerYear(self):
        return self.driver.find_element(*Cart.orderCustomerYear)
    
    def clickPurchase(self):
        return self.driver.find_element(*Cart.orderPurchaseButton)
    
    def sayPurchaseSuccess(self):
        return self.driver.find_element(*Cart.orderSuccessPurchase)