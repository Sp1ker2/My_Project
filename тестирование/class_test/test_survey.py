import unittest
from testing_class import AnonimServey


class TestAnonim(unittest.TestCase):
    def test_store(self):
        queistion = 'Langueage : '
        my_survey = AnonimServey(queistion)
        """тут в переменую передаём класс"""
        my_survey.store_response('java')
        self.assertIn('java', my_survey.responses)
        """а вот тут проверка идёт"""

    def test_five_responses(self):
        """5 ответов """
        queistion = 'Langueage : '
        my_survey = AnonimServey(queistion)
        responses12 = ['java', 'php', 'html', 'python', 'c++']
        """это массив  языков"""
        for response in responses12:
            my_survey.store_response(response)
        """тут это мы розбиваем на части"""
        for response in responses12:
            self.assertIn(response, my_survey.responses)
            """тут проверка есть ли он в массиве"""


if __name__ == '__name__':
    unittest.main()
