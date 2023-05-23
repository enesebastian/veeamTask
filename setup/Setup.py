from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait




def setup():
    chrome_options = Options()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
    wait = WebDriverWait(driver, 15)
    driver.implicitly_wait(20)
    return driver, wait
