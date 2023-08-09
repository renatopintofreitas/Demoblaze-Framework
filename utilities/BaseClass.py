from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
import logging
import inspect
import os

from pageObjects.HomePage import loginForm

@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        #log_directory = r"D:\DevLibrary\python\Demoblaze Framework\reports"
        log_directory = r"C:\REPORTS"
        log_filepath = os.path.join(log_directory, 'logfile.log')
        fileHandler = logging.FileHandler(log_filepath)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        
        return logger
    
    
    def wait_for_alert(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        return alert
    
    
    def wait_for_form(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((loginForm)))
        