from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # Проверяем что в корзине нет товаров
    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "There are items in the cart but " \
                                                                            "should not"

    # Проверяем что есть сообщение о том что корзина пуста
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), 'Empty basket message is not ' \
                                                                                'presented, but should be'
