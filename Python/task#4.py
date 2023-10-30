class Fruits():
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
fruits = []
def enter_1():
    name = input('введите название фрукта :\t')
    color = input('введите  цвет фрукта :\t')
    while True:
        weight = input('введите вес фрукта :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    fruits.append(Fruits(name.title(), color.title(), weight))
def conclusion_2():
    for i in fruits:
        print('————')
        print(i.name)
        print('цвет фрукта :\t', i.color)
        print('вес  фрукта :\t', i.weight, 'г')
    print('————')
while True:
    menu = input(f'''1 - Заполнить фрукт
2 - Вывести фрукты
3 - Выход\n''')
    match menu:
        case '1':
            enter_1()
        case '2':
            conclusion_2()
        case '3':
            break
