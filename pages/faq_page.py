import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import Urls
from locators import FaqLocators

class QuestionsPage:
    
    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.main_page)
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self, driver):
        element = driver.find_element(By.CLASS_NAME, "accordion")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, driver, index):
        question_locator = (
            FaqLocators.question[0],
            FaqLocators.question[1].format(index),
        )
        question = WebDriverWait(driver, 10).until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, driver, index):
        answers_locator = (FaqLocators.answer[0], FaqLocators.answer[1].format(index))
        answers = driver.find_element(*answers_locator)
        return answers.text
