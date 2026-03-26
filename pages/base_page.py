import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент")
    def find_element(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))
    
    @allure.step("Кликнуть на элемент")
    def click(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()
        return element
    
    @allure.step("Ввести текст")
    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        return element
    
    @allure.step("Получить текст")
    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text