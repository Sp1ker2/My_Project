import requests
import random

headers = {'Accept': '*/*',
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"}
base_url = 'https://swapi.dev/api/'


def func(*func):
    random.choice(func)()


def film(number):
    try:
        url_film = f"""{base_url}films/{number}/"""
        req_film = requests.get(url=url_film, headers=headers)
        src = req_film.json()
        print(src['title'])
    except KeyError:
        print('нету инфомации об єтом фильме  попробуйте другой ')


def people(number):
    try:
        url_people = f"""{base_url}people/{number}/"""
        req_people = requests.get(url=url_people, headers=headers)
        src = req_people.json()
        print(src['name'])
    except KeyError:
        print('нету инфомации об єтом персонаже попробуйте другого')


def starship(number):
    try:
        url_starships = f"""{base_url}starships/{number}/"""
        req_starships = requests.get(url=url_starships, headers=headers)
        src = req_starships.json()
        print(src['name'])
    except KeyError:
        print('нету такого корабля попробуйте другой запрос')


def vehicle(number):
    try:
        url_vehicles = f"""{base_url}vehicles/{number}/"""
        req_vehicles = requests.get(url=url_vehicles, headers=headers)
        src = req_vehicles.json()
        print(src['name'])
    except KeyError:
        print('нету такого средства передвежения попробуйте другое')


def specie(number):
    try:
        url_species = f"""{base_url}species/{number}/"""
        req_specie = requests.get(url=url_species, headers=headers)
        src = req_specie.json()
        print(src['name'])
    except KeyError:
        print('нету такой раси попробуйте другое')


def planet(number):
    try:
        url_planets = f"""{base_url}planets/{number}/"""
        req_planets = requests.get(url=url_planets, headers=headers)
        src = req_planets.json()
        print(src['name'])

    except KeyError:
        print('нету такой планети поробуйте что от другое')


def films():
    films = int(input("""1 - Показать конкретный фильм
2 - Показать первый фильм
3 - Показать случайный фильм
0 - Назад
    """))
    while True:
        match films:
            case 1:
                film(int(input('enter film number ')))
                break
            case 2:
                film(1)
                break
            case 3:
                film(int(random.randint(1, 6)))
                break
            case 0:
                break


def peoples():
    while True:
        peoples = input("""1 - Показать конкретный персонажа
2 - Показать первого персонажа
3 - Показать случайного персонажа
0 - Назад
""")
        match peoples:
            case '1':
                people(int(input('enter people number ')))
                break
            case '2':
                people(1)
                break
            case '3':
                people(int(random.randint(1, 83)))
                break
            case '0':
                break


def starships():
    while True:
        starships = input("""1 - Показать конкретный корабль
2 - Показать первий корабль
3 - Показать случайний корабль
0 - Назад
""")
        match starships:
            case '1':
                starship(int(input('enter starships number ')))
                break
            case '2':
                starship(9)
                break
            case '3':
                starship(int(random.randint(9, 17)))
                break
            case '0':
                break


def vehicles():
    while True:
        vehicles = input("""1 - Показать конкретную машину
2 - Показать первую машину
3 - Показать случайную машину
0 - Назад
""")
        match vehicles:
            case '1':
                vehicle(int(input('enter vehicles number ')))
                break
            case '2':
                vehicle(4)
                break
            case '3':
                vehicle(int(random.randint(4, 4)))
                break
            case '0':
                break


def species():
    species = input("""1 - Показать конкретную  разновидность
2 - Показать первую разновидность
3 - Показать случайную разновидность
0 - Назад """)
    while True:
        match species:
            case '1':
                specie(int(input('enter species number ')))
                break
            case '2':
                specie(1)
            case '3':
                specie(int(random.randint(1, 38)))
                break
            case '0':
                break


def planets():
    while True:
        planets = input("""1 - Показать конкретную планету
2 - Показать первую планету
3 - Показать случайную планету
0 - Назад """)
        match planets:
            case '1':
                planet(int(input('enter planets number ')))
                break
            case '2':
                planet(1)
                break
            case '3':
                planet(int(random.randint(1, 38)))
                break
            case '0':
                break


while True:
    star_wars = input("""— Энциклопедия Star Wars —
1 - Показать фильм
2 - Показать человека
3 - Показать планету
4 - Показать вид
5 - Показать корабль
6 - Показать технику
7 - Показать случайный элемент любого списка
0 - Выход
""")

    match star_wars:
        case '1':
            films()
        case '2':
            peoples()
        case '3':
            planets()
        case '4':
            species()
        case "5":
            starships()
        case "6":
            vehicles()
        case '7':
            func(films, peoples, planets, species, starships, vehicles)
        case '0':
            break
