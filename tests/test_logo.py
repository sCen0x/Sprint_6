import allure
import pytest
from pages.logo_page import LogoPage


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser(driver)
        logo_page.click_order_button(driver)
        logo_page.click_scooter_button(driver)
        logo_page.should_main_page_url(driver)

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, driver):
        logo_page = LogoPage(driver)
        logo_page.open_browser(driver)
        logo_page.click_dzen_button(driver)
        logo_page.switching_to_the_tab(driver)
        logo_page.wait_for_page_load(driver)
        logo_page.should_dzen_url(driver)