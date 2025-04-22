"""#task5
Расширить программу с фрутками до программы работы с едой, где на выбор есть:
Овощи
Фрукты
Ягоды
Готовое продовольствие

Готовое продовольствие делить на горячее/холодное и жидкое/твердое
Готовое продовольствие-> горячее/холодное
                                |
                                \
                                  > жидкое/твердое
ну оно может быть одновременно горячее жидкое
и холодное твердое
Реализовать к каждому цену, и подсчет итоговой цены корзины, в нашем случае - массива продуктов

Свойства овощей те же что и у фруктов, добавляется цена за килограм
У фруктов добавляется поле цены за килограм
У ягод те же поля что и у фрутков, добавляется цена за килограм
Готовое продовольствие с полями имени, веса, цены не за килограм, а итоговой

В выводе корзины выводить сколько фруктов, овощей, ягод и продовольствия в корзине
изначально такой вывод

1 - заполнить товар
2 - вывести корзину
3 - выход
выбираешь заполнение
выходит это:
1-овощ
2 - фрукт
и так далее
выбираешь овощ и дает запрос на поля название, цвет, и тд потом возвращается сюда


"""


class Fruits():
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Vegetables():
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Berries():
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Hotmeat():
    def __init__(self, name, color, weight, price):
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Hot(Hotmeat):
    def __init__(self, name, color, weight, price):
        super().__init__(name, color, weight, price)
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Freeze(Hotmeat):
    def __init__(self, name, color, weight, price):
        super().__init__(name, color, weight, price)
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Liquid(Hotmeat):
    def __init__(self, name, color, weight, price):
        super().__init__(name, color, weight, price)
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


class Solid(Hotmeat):
    def __init__(self, name, color, weight, price):
        super().__init__(name, color, weight, price)
        self.name = name
        self.color = color
        self.weight = weight
        self.price = price


price_all = []
fruits = []
vegetables = []
berries = []

freeze_liquid = []
freeze_solid = []
hot_liquid = []
hot_solid = []


def enter_1_vegetables():
    name = input('введите название овоща :\t')
    color = input('введите  цвет овоща :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')

    price = int(price)
    weight = int(weight)
    vegetables.append(Vegetables(name.title(), color.title(), weight, price))
    price_all.append(price * weight)



def enter_1_fruits():
    name = input('введите название фрукта :\t')
    color = input('введите  цвет фрукта :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    price = int(price)
    weight = int(weight)
    fruits.append(Fruits(name.title(), color.title(), weight, price))
    price_all.append(price * weight)


def enter_1_berries():
    name = input('введите название ягоди :\t')
    color = input('введите  цвет ягоди :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
        break
    price = int(price)
    weight = int(weight)
    berries.append(Berries(name.title(), color.title(), weight, price))
    price_all.append(price * weight)


def enter_1_hotmeat_liquid():
    name = input('введите название жидкого блюда  :\t')
    color = input('введите  цвет жидкого блюда :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    price = int(price)
    hot_liquid.append(Liquid(name.title(), color.title(), weight, price))
    price_all.append(price)


def enter_1_hotmeat_solid():
    name = input('введите название твердого блюда :\t')
    color = input('введите  цвет твердого блюда :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    price = int(price)
    hot_solid.append(Solid(name.title(), color.title(), weight, price))
    price_all.append(price)


def enter_1_hotmeat_freeze_liquid():
    name = input('введите название овоща :\t')
    color = input('введите  цвет овоща :\t')
    while True:
        price = input('введите цену ягоди :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес ягоди :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    price = int(price)
    freeze_liquid.append(Solid(name.title(), color.title(), weight, price))
    price_all.append(price)


def enter_1_hotmeat_freeze_solid():
    name = input('введите название овоща :\t')
    color = input('введите  цвет овоща :\t')
    while True:
        price = input('введите цену жидкого :\t')
        if price.isdigit():
            break
        print('введите положительное число ')
    while True:
        weight = input('введите вес жидкого :\t')
        if weight.isdigit():
            break
        print('введите положительное число ')
    price = int(price)
    freeze_solid.append(Solid(name.title(), color.title(), weight, price))
    price_all.append(price)


def enter_1_hotmeat():
    while True:
        meat = input(f'''1 - жидкое
2 - твердое
3 - break \n''')
        match meat:
            case '3':
                break
        h_o_f = input(f'''вам подогреть блюдо :
1 - да
2 - нет\n''')
        match meat, h_o_f:
            case '1', '1':
                enter_1_hotmeat_liquid()
            case '2', '1':
                enter_1_hotmeat_solid()
            case '1', '2':
                enter_1_hotmeat_freeze_liquid()
            case '2', '2':
                enter_1_hotmeat_freeze_solid()

def all_price():
    s = 0
    for i in price_all:
        s += i
        print(s)

def enter_params(eat):
    while True:

        match eat:
            case '1':
                enter_1_vegetables()
                break
            case '2':
                enter_1_fruits()
            case '3':
                enter_1_berries()
            case '4':
                enter_1_hotmeat()
            case '5':
                break
        break


def conclusion_2():
    print('ваш чек\n')
    if len(fruits) != 0:
        print('fruits')
        for i in fruits:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(vegetables) != 0:
        print('vegetables')
        for i in vegetables:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(berries) != 0:
        print('berries')
        for i in berries:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(hot_solid) != 0:
        print('hot solid')
        for i in hot_solid:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(hot_liquid) != 0:
        print('hot liquid')
        for i in hot_liquid:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(freeze_solid) != 0:
        print('freeze solid')
        for i in freeze_solid:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    if len(freeze_liquid) != 0:
        print('freeze liquid')
        for i in freeze_liquid:
            print('————')
            print(i.name)
            print('цвет фрукта :\t', i.color)
            print('вес  фрукта :\t', i.weight, 'kг')
        print('————')
    v = 0
    for i in price_all:
        v += i
    print(v)
menu = input(f'''1 - Заполнить товар
2 - Вывести товар
3 - Выход\n''')
eat = input(f'''1 - Овощи
2 - Фрукты
3 - Ягоды
4 - Готовое продовольствие
5 - break\n''')
while True:

    match menu:
        case '1':
            enter_params(eat)
        case '2':
            conclusion_2()
        case '3':
            break
