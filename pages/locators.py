from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, '.basket_summary')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_CART_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1) .alertinner strong")
    PRODUCT_PRICE_CART_MESSAGE = (By.CSS_SELECTOR, ".alert div p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1) div")
