import allure
from data import Urls
from locators import OrderLocators, LogoLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LogoPage:
    
    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.main_page)
        return self

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_order_button(self, driver):
        driver.find_element(*OrderLocators.order_button_header).click()
        return self

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self, driver):
        driver.find_element(*LogoLocators.scooter_button).click()
        return self

    @allure.step("Клик по лого 'Яндекс'")
    def click_dzen_button(self, driver):
        driver.find_element(*LogoLocators.yandex_button).click()
        return self

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self, driver):
        driver.switch_to.window(driver.window_handles[1])
        return self

    @allure.step("Ожидание загрузки страницы")
    def wait_for_page_load(self, driver):
        WebDriverWait(driver, 10).until(ec.url_to_be(Urls.dzen))
        return self

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self, driver):
        assert driver.current_url == Urls.dzen
        return self

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self, driver):
        assert driver.current_url == Urls.main_page
        return self
