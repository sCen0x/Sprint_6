import allure
from locators import OrderLocators
from data import Urls
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

class OrderPage(BasePage):
    
    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.main_page)
        return self

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_first_button(self, driver):
        self.click(OrderLocators.order_button_header)
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self, driver):
        element = self.find_element(OrderLocators.order_button_center)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return self

    @allure.step("Заполнение поля Имя")
    def user_name(self, driver, name):
        self.input_text(OrderLocators.name, name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, driver, last_name):
        self.input_text(OrderLocators.last_name, last_name)
        return self

    @allure.step("Заполнение поля Адрес")
    def user_address(self, driver, address):
        self.input_text(OrderLocators.address, address)
        return self

    @allure.step("Заполнение поля Станция метро")
    def metro(self, driver, metro):
        field = self.find_element(OrderLocators.metro_station)
        field.click()
        field.send_keys(metro)
        
        station_locator = (
            OrderLocators.metro_station_option[0],
            OrderLocators.metro_station_option[1].format(metro)
        )
        self.click(station_locator)
        return self

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, driver, phone):
        self.input_text(OrderLocators.phone_number, phone)
        return self

    @allure.step('Клик по кнопке "Далее"')
    def click_button_next(self, driver):
        self.click(OrderLocators.next_button)
        return self

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, driver, data):
        field = self.find_element(OrderLocators.date_delivery)
        field.click()
        field.send_keys(data)
        field.send_keys(Keys.ENTER)
        return self

    @allure.step("Заполнение поля Срок аренды")
    def rental_time(self, driver, day):
        self.click(OrderLocators.rent_time)
        
        rent_option_locator = (
            OrderLocators.select_rent_time[0],
            OrderLocators.select_rent_time[1].format(day),
        )
        self.click(rent_option_locator)
        return self

    @allure.step("Выбор цвета самоката")
    def checkbox_color(self, driver, color):
        if color == "чёрный жемчуг":
            self.click(OrderLocators.black_color_checkbox)
        elif color == "серая безысходность":
            self.click(OrderLocators.grey_color_checkbox)
        return self

    @allure.step("Заполнение поля Комментарии для курьера")
    def comment_for_courier(self, driver, comment):
        self.input_text(OrderLocators.comment, comment)
        return self

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self, driver):
        self.click(OrderLocators.order_button)
        return self

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self, driver):
        self.click(OrderLocators.yes_button)
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, driver):
        text = self.get_text(OrderLocators.order_completed)
        assert "Заказ оформлен" in text
        return self

    @allure.step("Позитивный сценарий")
    def user_rent_order(
        self,
        driver,
        name,
        last_name,
        address,
        metro,
        number,
        delivery_date,
        rent_days,
        colour,
        comment,
    ):
        self.user_name(driver, name)
        self.user_last_name(driver, last_name)
        self.user_address(driver, address)
        self.metro(driver, metro)
        self.user_phone(driver, number)
        self.click_button_next(driver)
        self.date_of_delivery(driver, delivery_date)
        self.rental_time(driver, rent_days)
        self.checkbox_color(driver, colour)
        self.comment_for_courier(driver, comment)
        self.click_button_order(driver)
        self.click_button_confirmations(driver)
        self.confirmation_window(driver)
        return self
