import allure
from locators import OrderLocators
from data import Urls
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class OrderPage:
    
    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.main_page)
        return self

    @allure.step("Клик по кнопке Заказать в шапке")
    def click_first_button(self, driver):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.order_button_header)).click()
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self, driver):
        element = WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.order_button_center))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return self

    @allure.step("Заполнение поля Имя")
    def user_name(self, driver, name):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.name)).send_keys(name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, driver, last_name):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.last_name)).send_keys(last_name)
        return self

    @allure.step("Заполнение поля Адрес")
    def user_address(self, driver, address):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.address)).send_keys(address)
        return self

    @allure.step("Заполнение поля Станция метро")
    def metro(self, driver, metro):
        field = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.metro_station))
        field.send_keys(metro)
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.list_station)).click()
        return self

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, driver, phone):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.phone_number)).send_keys(phone)
        return self

    @allure.step('Клик по кнопке "Далее"')
    def click_button_next(self, driver):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.next_button)).click()
        return self

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, driver, data):
        field = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.date_delivery))
        field.send_keys(data)
        field.send_keys(Keys.ENTER)
        return self

    @allure.step("Заполнение поля Срок аренды")
    def rental_time(self, driver, day):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.rent_time)).click()
        select_rent_time_locator = (
            OrderLocators.select_rent_time[0],
            OrderLocators.select_rent_time[1].format(day),
        )
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(select_rent_time_locator)).click()
        return self

    @allure.step("Выбор цвета самоката")
    def checkbox_color(self, driver, color):
        if color == "чёрный жемчуг":
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.black_color_checkbox)).click()
        elif color == "серая безысходность":
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.grey_color_checkbox)).click()
        return self

    @allure.step("Заполнение поля Комментарии для курьера")
    def comment_for_courier(self, driver, comment):
        WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.comment)).send_keys(comment)
        return self

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self, driver):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.order_button)).click()
        return self

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self, driver):
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable(OrderLocators.yes_button)).click()
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, driver):
        text = (
            WebDriverWait(driver, 10).until(ec.presence_of_element_located(OrderLocators.order_completed)).text
        )
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
