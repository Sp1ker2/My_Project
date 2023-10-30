from linkes_list import LinkedList
import time
import random
length = 10000
print(f"количество елементов в каждом массиве -  {length}")

start = time.monotonic()
my_link = LinkedList()
my_array = []


def random_gen_link():
    for i in range(0, length):
        x1 = random.randint(0, 1000)
        my_link.append(x1)
    # my_link.show()


random_gen_link()
# print("--- %s seconds ---" % (time.time() - start_time) + 'link test')
print(f'Время random link {time.monotonic() - start} s.')
start = time.monotonic()


def append_link():
    for i in range(0, length):
        my_link.append(i)
    # my_link.show()


append_link()
print(f'Время append link {time.monotonic() - start} s.')
start = time.monotonic()


def push_front_link():
    for i in range(0, length):
        my_link.push_front(i)
    # my_link.show()


push_front_link()
print(f'Время push front link {time.monotonic() - start} s.')
start = time.monotonic()


def insert_link():
    for i in range(0, length):
        my_link.append(i)
    my_link.insert(length/2, "середина")
    # my_link.show()


insert_link()
print(f'Время insert link {time.monotonic() - start} s.')

start = time.monotonic()
def random_gen_array():
    for i in range(0, length):
        x1 = random.randint(0, 1000)
        my_array.append(x1)
    # print(my_array)


random_gen_array()
# print("--- %s seconds ---" % (time.time() - start_time) + 'link test')
print(f'Время random array {time.monotonic() - start} s.')
start = time.monotonic()


def append_array():
    for i in range(0, length):
        my_array.append(i)
    # print(my_array)


append_array()
print(f'Время append array {time.monotonic() - start} s.')
start = time.monotonic()


def push_front_array():
    for i in range(0, length):
        my_array.insert(0, i)
    # print(my_array)


push_front_array()
print(f'Время push front array {time.monotonic() - start} s.')
start = time.monotonic()


def insert_array():
    for i in range(0, length):
        my_array.append(i)
    my_array.insert(5000, "середина")
    # print(my_array)


insert_array()
print(f'Время insert array {time.monotonic() - start} s.')
