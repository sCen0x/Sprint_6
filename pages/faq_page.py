import allure
from pages.base_page import BasePage

from data import Urls
from locators import FaqLocators


class QuestionsPage(BasePage):

    @allure.step("Открытие браузера")
    def open_browser(self,):
        self.open_url(Urls.main_page)
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self):
        self.scroll_to_element(FaqLocators.faq_block)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, index):
        question_locator = (
            FaqLocators.question[0],
            FaqLocators.question[1].format(index),
        )
        question = self.click(question_locator)
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, index):
        answers_locator = (
            FaqLocators.answer[0],
            FaqLocators.answer[1].format(index)
        )
        return self.get_text(answers_locator)
