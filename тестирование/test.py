import unittest
from full_name import full_name

"""с докуметнат fuull_name функцию"""


class NamaTestCase(unittest.TestCase):
    """берём  модуль unittest и определёний метод """
    """тестирование файла full_name"""
    """  'test_ '   мы тут написали не просто так он будет выполнятся любая функция где начало со слова test_"""

    def test_first_last_name(self):
        """enter 'Bogdan Prihodko' and try ? """
        format_name = full_name('Bogdan', 'Prihodko')
        self.assertEqual(format_name, 'Bogdan Prihodko')

    """а если я хочу полное фио но Ф не обезательно"""
    def test_first_last_middle_name(self):
        format_name = full_name('Bogdan', 'Prihodko','Andreevich')
        """и теперь идём ф первую функцию и редактируем под фио """
        self.assertEqual(format_name, 'Bogdan Prihodko Andreevich')




"""есть ошибка там и крч всегда писать и меньше парится"""
if __name__ == '__name__':
    unittest.main()
# __name__
