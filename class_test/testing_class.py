class AnonimServey():
    """"анонимный опрос"""

    def __init__(self, question):
        self.question = question
        """ложим в список потомучто переменнная будет всё время перезаписиваться"""
        self.responses = []

    def show_question(self):
        """вывод вопроса"""
        print(self.question)

    def store_response(self, new_response):
        """сохранение одного ответа"""
        self.responses.append(new_response)
        """так как это класс и список мы можем вот такое сделать"""
    def show_results(self):
        """вывод получаемого ответов"""
        print("вывод получаемого ответов")
        for response in self.responses:
            print(' - ' + response)

# anonim = AnonimServey('gey?')
# anonim.show()
# anonim.save('no')
# anonim.all_responses()