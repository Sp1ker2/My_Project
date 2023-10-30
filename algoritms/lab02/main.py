import random
import time
import sys
sys.setrecursionlimit(10**9)
"""Insertion Sort або Selection Sort +
Bubble Sort та / або Cocktail Sort +
Quick Sort 
Merge Sort 
Count Sort 
Radix Sort +
Basket Sort +
Timsort +
Binary tree sort +"""

arr = []
length = 100000
for i in range(0, length):
    r = random.randint(0, 1000)
    arr.append(r)
# print(arr)
# Insertion Sort
start = time.monotonic()


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


insertion_sort_arr = insertion_sort(arr)
# print(insertion_sort_arr)
print(f"Insertion Sort {time.monotonic() - start} s.")


# Quick Sort

start = time.monotonic()
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Проходим по массиву с конца до текущего элемента
        for j in range(n - 1, i, -1):
            # Если текущий элемент меньше предыдущего, то меняем их местами
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

buble_sort_arr = bubble_sort(arr)
# print(buble_sort_arr)
print(f"Bubble Sort  {time.monotonic() - start} s.")


# Quick Sort

start = time.monotonic()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quick_sort(left) + [pivot] + quick_sort(right)


quick_sort_arr = arr
# print(quick_sort_arr)
print(f"Quick Sort {time.monotonic() - start} s.")

start = time.monotonic()


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # разбиваем массив на две части
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    # рекурсивно вызываем функцию merge_sort() для каждой половины
    left = merge_sort(left)
    right = merge_sort(right)

    # объединяем две отсортированные части
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # сравниваем элементы из двух списков и добавляем наименьший в результирующий список
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем оставшиеся элементы из левого и правого списков
    result += left[i:]
    result += right[j:]

    return result


sorted_merge_arr = arr
# print(sorted_merge_arr)
print(f"Merge Sort {time.monotonic() - start} s.")

start = time.monotonic()


def count_sort(arr):
    max_value = max(arr)
    counts = [0] * (max_value + 1)

    # считаем количество вхождений каждого элемента в список
    for num in arr:
        counts[num] += 1

    # строим новый отсортированный список
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr += [i] * counts[i]

    return sorted_arr


count_sort_arr = arr
# print(count_sort_arr)
print(f"Count Sort {time.monotonic() - start} s.")

start = time.monotonic()


def radix_sort(arr):
    max_value = max(arr)
    exp = 1

    # сортируем элементы по разрядам
    while max_value // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


def counting_sort(arr, exp):
    n = len(arr)
    counts = [0] * 10

    # считаем количество вхождений каждого элемента в список
    for i in range(n):
        index = arr[i] // exp
        counts[index % 10] += 1

    # вычисляем позиции элементов в отсортированном списке
    for i in range(1, 10):
        counts[i] += counts[i - 1]

    # строим новый отсортированный список
    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        sorted_arr[counts[index % 10] - 1] = arr[i]
        counts[index % 10] -= 1

    return sorted_arr


radix_sort_arr = radix_sort(arr)
# print(radix_sort_arr)
print(f"Radix Sort  {time.monotonic() - start} s.")
start = time.monotonic()


def bucket_sort(arr):
    # Определяем количество корзин (бакетов)
    num_buckets = len(arr)
    # Создаем пустые корзины
    buckets = [[] for _ in range(num_buckets)]
    # Распределяем элементы по корзинам
    for num in arr:
        index = num * num_buckets // (max(arr) + 1)
        buckets[index].append(num)
    # Сортируем каждую корзину и объединяем их
    sorted_arr = []
    for bucket in buckets:
        sorted_arr += sorted(bucket)
    return sorted_arr


basket_sort_arr = bucket_sort(arr)
# print(basket_sort_arr)
print(f"Basket Sort  {time.monotonic() - start} s.")
