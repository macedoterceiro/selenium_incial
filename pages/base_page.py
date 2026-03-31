from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class base_page:
    def __init__(self, driver, base_url="https://automationexercise.com/"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10
    
    def find_element(self, by, value):
        return self.driver.find_element(by, value)
    
    def wait_and_find_element(self, by, value, timeout=None):
        to = timeout or self.timeout
        WebDriverWait(self.driver, to).until(EC.presence_of_element_located((by, value)))
        return self.find_element(by, value)
    
    def open(self, url=""):
        self.driver.get(self.base_url + url)

    def hover_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def wait_element(self, by, value, timeout=None):
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            print(f"Elemento com {by}='{value}' não encontrado após {timeout or self.timeout} segundos.")
            self.driver.quit()
            raise