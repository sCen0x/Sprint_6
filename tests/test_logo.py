import allure
import pytest
from pages.logo_page import LogoPage


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser()
        logo_page.click_order_button()
        logo_page.click_scooter_button()
        logo_page.should_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser()
        logo_page.click_dzen_button()
        logo_page.switching_to_the_tab()
        logo_page.wait_for_page_load()
        logo_page.should_dzen_url()