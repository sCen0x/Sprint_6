from selenium.webdriver.common.by import By


class FaqLocators:
    question = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    answer = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]
    faq_block = [By.CLASS_NAME, "accordion"]


class LogoLocators:
    scooter_button = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_button = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")


class OrderLocators:
    order_button_header = [By.CLASS_NAME, "Button_Button__ra12g"]
    order_button_center = (By.XPATH, "//div[contains(@class, 'FinishButton')]//button[text()='Заказать']")

    name = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    metro_station_option = [By.XPATH, "//div[contains(text(), '{}')]"]
    phone_number = [By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']",]
    next_button = [By.XPATH, ".//button[text()='Далее']"]
    date_delivery = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rent_time = [By.XPATH, '//div[text()="* Срок аренды"]']
    select_rent_time = [By.XPATH, '//div[text()="{}"]']
    black_color_checkbox = [By.XPATH, '//label[@for="black"]']
    grey_color_checkbox = [By.XPATH, '//label[@for="grey"]']
    comment = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH,'//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]',]
    yes_button = [By.XPATH, ".//button[text()='Да']"]
    order_completed = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']
