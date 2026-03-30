import os.path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def parse_config():
    chrome_options = Options()
    #chrome_options.add_argument("--headless") # Roda sem abrir a janela
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=1920,1080")

    homedir = os.path.expanduser("~")
    chrome_options.binary_location = f"{homedir}/chrome-linux64/chrome"
    webdriver_service = Service(f"{homedir}/chromedriver-linux64/chromedriver")

    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    return driver