from base_config import parse_config
from methods import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_checkbox():

    driver = parse_config()

    try:
        driver.get("https://www.qa-practice.com/")
        checkbox_menu = wait_until_clickable(driver, By.XPATH, "//a[(text()='Single checkbox')]", timeout=15)
        checkbox_menu.click()

        checkbox_item = wait_until_clickable(driver, By.ID, "id_checkbox_0", timeout=15)
        if not checkbox_item.is_selected():
            checkbox_item.click()
        
        assert checkbox_item.is_selected(), "O checkbox não foi selecionado corretamente."

        submit_button = wait_until_clickable(driver, By.ID, "submit-id-submit", timeout=15)
        submit_button.click()

        expectedText = "Selected checkboxes:";
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "result"), expectedText))

        print("Teste passou: Página carregada com sucesso.")

    except Exception as e:
        print(f"Teste falhou: {e}")

if __name__ == "__main__":
    select_checkbox()