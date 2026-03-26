import allure
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
from data import Urls
from locators import FaqLocators


class QuestionsPage(BasePage):

    @allure.step("Открытие браузера")
    def open_browser(self, driver):
        driver.get(Urls.main_page)
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self, driver):
        element = driver.find_element(*FaqLocators.faq_block)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, driver, index):
        question_locator = (
            FaqLocators.question[0],
            FaqLocators.question[1].format(index),
        )
        question = self.wait.until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, driver, index):
        answers_locator = (FaqLocators.answer[0], FaqLocators.answer[1].format(index))
        answers = self.find_element(answers_locator)
        return answers.text
