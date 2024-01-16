from testing_class import AnonimServey

question = 'why do you like language programaning?'
my_survey = AnonimServey(question)
my_survey.show_question()
print('tab Q when to exit')
while True:
    response = input('language : ')
    if response == 'Q':
        break
    my_survey.store_response(response)
my_survey.show_results()
