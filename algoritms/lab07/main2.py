book = dict()
book['apple'] = 0.34
book['milk'] = 0.31
book['juice'] = 0.45
print(book,'заповнення словаря')
# обновления данних
book['apple'] = 0.12
print(book,'оновлення данних')
del book['milk']
print(book,'видалення одного ключа а з ним і значення')
book.clear()
print(book,'видалення усієї таблиці ')
