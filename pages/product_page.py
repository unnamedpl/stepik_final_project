from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # Проверяем наличие кнопки "Добавить в корзину" на странице
    def should_be_add_button_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button 'Add to basket' is not presented"

    # Добавляем товар в корзину и выводим код в консоль
    def should_be_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    # Проверяем текст успешного добавления в корзину
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_CART_MESSAGE), 'Message of Success added ' \
                                                                                        'product in basket not found '

    # Проверяем название добавленого товара в корзину
    def should_be_correct_name_in_basket(self):
        name_product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART_MESSAGE).text
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_product == name_product_added, "Product name is different"

    # Проверяем цену добавленого товара в корзину
    def should_be_correct_price_in_basket(self):
        price_product_added = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert price_product_added == price_product, "Product price is different"
