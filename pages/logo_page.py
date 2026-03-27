import allure
from data import Urls
from locators import OrderLocators, LogoLocators

from pages.base_page import BasePage

class LogoPage(BasePage):
    
    @allure.step("Открытие браузера")
    def open_browser(self):
        self.open_url(Urls.main_page)
        return self

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_order_button(self):
        self.click(OrderLocators.order_button_header)
        return self

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self):
        self.click(LogoLocators.scooter_button)
        return self

    @allure.step("Клик по лого 'Яндекс'")
    def click_dzen_button(self):
        self.click(LogoLocators.yandex_button)
        return self

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self):
        self.switch_to_tab(1)
        return self

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self):
        self.wait_url_to_be(Urls.dzen)
        return self

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self):
        assert self.get_current_url() == Urls.dzen
        return self

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self):
        assert self.get_current_url() == Urls.main_page
        return self
