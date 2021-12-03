from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Should be login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Should be login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Should be register form"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
