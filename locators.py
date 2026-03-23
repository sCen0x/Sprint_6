from selenium.webdriver.common.by import By

class FaqLocators:
    question = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    answer = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]

class LogoLocators:
    scooter_button = [By.XPATH, ".//a[@href='/']"]
    yandex_button = [By.XPATH, ".//a[@href='//yandex.ru']"]

class OrderLocators:
    order_button_header = [By.XPATH, "//button[text()='Заказать']"]
    order_button_center = [By.XPATH, '(//button[text()="Заказать"])[2]']
    name = [By.XPATH, "//input[@placeholder='* Имя']"]
    last_name = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro_station = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    list_station = [By.XPATH, "//li[@data-index='0']"]
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
