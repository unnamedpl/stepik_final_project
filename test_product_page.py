from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest
import time


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button_to_basket()
    page.should_be_add_product_to_basket()
    page.should_be_success_message()
    page.should_be_correct_name_in_basket()
    page.should_be_correct_price_in_basket()
