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
    
    @allure.step("Открыть URL")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element
    
    @allure.step("Переключиться на вкладку")
    def switch_to_tab(self, tab_index=1):
        self.wait.until(lambda driver: len(driver.window_handles) > tab_index)
        self.driver.switch_to.window(self.driver.window_handles[tab_index])

    @allure.step("Ожидать URL")
    def wait_url_to_be(self, url):
        self.wait.until(ec.url_to_be(url))
    
    @allure.step("Ожидать, что URL содержит текст")
    def wait_url_contains(self, text):
        self.wait.until(ec.url_contains(text))

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Выполнить скрипт")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)