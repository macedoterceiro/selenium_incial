from pages.base_page import BasePage
from pages.home_page import HomePage
from utils import users

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "login"

    def enter_email(self, email):
        email_input = self.wait_and_find_element("name", "email")
        email_input.clear()
        email_input.send_keys(email)
    
    def enter_password(self, password):
        password_input = self.wait_and_find_element("name", "password")
        password_input.clear()
        password_input.send_keys(password)
    
    def click_login(self):
        login_button = self.wait_and_find_element("xpath", "//button[@text()=contains(., 'Login') and @type='submit']")
        login_button.click()

    def login(self, user):
        user = users.get_user(user)
        if not user:
            print("User not found")
            return
        if 'login' not in self.url:
            self.driver.get('https://automationexercise.com/login')

        self.enter_email(user["email"])
        self.enter_password(user["password"])
        self.click_login()

    def login_with_valid_user(self):
        self.login("valid")
        return HomePage(self.driver)

    def login_with_invalid_user(self):
        self.login("invalid")
        return self.driver.find_element("xpath", "//p[contains(text(), 'Your email or password is incorrect!')]").text