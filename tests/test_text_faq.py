import allure
import pytest
from pages.faq_page import QuestionsPage
from data import QuestionsAndAnswers


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description(
        "Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ"
    )
    @pytest.mark.parametrize(
        "index, question, answer", QuestionsAndAnswers.questions_and_answers
    )
    def test_check_question_and_answer(self, driver, index, question, answer):
        page = QuestionsPage()
        page.open_browser(driver)
        page.scroll_to_faq(driver)
        question_text = page.get_question(driver, index)
        answer_text = page.get_answers(driver, index)
        assert question_text == question
        assert answer_text == answer
