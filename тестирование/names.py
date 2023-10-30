from full_name import full_name

"""тут мы импортируем файл а потом функцию   """
print('why are you neeed quit tab Q ')
while True:
    first = input('\neneter your name: ')
    if first == 'Q':
        break
    last = input('\nenter your surname: ')
    if last == 'Q':
        break
    format_name = full_name(first, last)
    print("\t format "+ format_name)

