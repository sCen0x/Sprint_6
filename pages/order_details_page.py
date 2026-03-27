import allure
from locators import OrderLocators
from data import Urls
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class OrderPage(BasePage):
    
    @allure.step("Открытие браузера")
    def open_browser(self):
        self.open_url(Urls.main_page)
        return self

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_first_button(self):
        self.click(OrderLocators.order_button_header)
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self):
        self.scroll_to_element(OrderLocators.order_button_center)
        self.click(OrderLocators.order_button_center)
        return self

    @allure.step("Заполнение поля Имя")
    def user_name(self, name):
        self.input_text(OrderLocators.name, name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, last_name):
        self.input_text(OrderLocators.last_name, last_name)
        return self

    @allure.step("Заполнение поля Адрес")
    def user_address(self, address):
        self.input_text(OrderLocators.address, address)
        return self

    @allure.step("Заполнение поля Станция метро")
    def metro(self, metro):
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
    def user_phone(self, phone):
        self.input_text(OrderLocators.phone_number, phone)
        return self

    @allure.step('Клик по кнопке "Далее"')
    def click_button_next(self):
        self.click(OrderLocators.next_button)
        return self

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, data):
        field = self.find_element(OrderLocators.date_delivery)
        field.click()
        field.send_keys(data)
        field.send_keys(Keys.ENTER)
        return self

    @allure.step("Заполнение поля Срок аренды")
    def rental_time(self, day):
        self.click(OrderLocators.rent_time)
        
        rent_option_locator = (
            OrderLocators.select_rent_time[0],
            OrderLocators.select_rent_time[1].format(day),
        )
        self.click(rent_option_locator)
        return self

    @allure.step("Выбор цвета самоката")
    def checkbox_color(self, color):
        if color == "чёрный жемчуг":
            self.click(OrderLocators.black_color_checkbox)
        elif color == "серая безысходность":
            self.click(OrderLocators.grey_color_checkbox)
        return self

    @allure.step("Заполнение поля Комментарии для курьера")
    def comment_for_courier(self, comment):
        self.input_text(OrderLocators.comment, comment)
        return self

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self):
        self.click(OrderLocators.order_button)
        return self

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self):
        self.click(OrderLocators.yes_button)
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        text = self.get_text(OrderLocators.order_completed)
        assert "Заказ оформлен" in text
        return self

    @allure.step("Позитивный сценарий")
    def user_rent_order(
        self,
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
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_button_next()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_button_order()
        self.click_button_confirmations()
        self.confirmation_window()
        return self
