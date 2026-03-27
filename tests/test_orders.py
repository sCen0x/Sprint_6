import allure
import pytest
from data import OrderData
from pages.order_details_page import OrderPage



class TestOrderPage:
    @allure.title("Проверка позитивного сценария заказа самоката")
    @allure.description(
        "Проверяем весь флоу позитивного сценария с двумя наборами данных"
    )
    @pytest.mark.parametrize(
        "button_method, data_order",
        [
            ("click_first_button", OrderData.first_order),
            ("click_second_button", OrderData.second_order),
        ],
    )
    def test_make_an_order(self, driver, data_order, button_method):
        page = OrderPage(driver)       
        page.open_browser()
        getattr(page, button_method)()
        page.user_rent_order(**data_order)
        page.confirmation_window()
