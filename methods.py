from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

def wait_until_clickable(browser, by, locator, timeout=10):
    try:
        return WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((by, locator)))
    except TimeoutException:
        print(f"Elemento não ficou clicável após {timeout} segundos.")
        return None

def wait_until_visible(browser, by, locator, timeout=10):
    try:
        return WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((by, locator)))
    except TimeoutException:
        print(f"Elemento não ficou visível após {timeout} segundos.")
        return None

def click_with_retry(browser, element, retries=3, delay=2):
    for attempt in range(retries):
        try:
            element.click()
            return  # Se o clique for bem-sucedido, retorna da função
        except ElementClickInterceptedException:
            print(f"Falha ao clicar. Tentativa {attempt + 1} de {retries}. Aguardando {delay} segundos...")
            time.sleep(delay)  # Espera antes de tentar novamente

def random_number(n):
    return random.randint(1, n)

def generate_random_string(size=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))

def generate_random_numbers(size=10):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(size))

def concat_strings(string1, string2):
    return string1 + ' ' + string2