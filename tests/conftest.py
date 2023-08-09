import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    

@pytest.fixture(scope="class")
def setup(request):
    
    browser_name = request.config.getoption("browser_name")
    
    if browser_name == "chrome":
        service_obj = Service("C:\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        
    elif browser_name == "firefox":
        service_obj = Service("C:\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        
    elif browser_name == "edge":
        service_obj = Service("C:\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/")    
    request.cls.driver = driver
    yield
    driver.close()
