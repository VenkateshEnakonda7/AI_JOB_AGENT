from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 2})

    service = Service('E:/Pyhton/AI_Job_Agent/chromedriver.exe')  # <--- Update your path
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    return driver
