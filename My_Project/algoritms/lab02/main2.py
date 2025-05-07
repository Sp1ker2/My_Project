import random
import time
import sys
sys.setrecursionlimit(10**9)
"""Insertion Sort або Selection Sort +
Bubble Sort та / або Cocktail Sort +
Quick Sort +
Merge Sort +
Count Sort +
Radix Sort +
Basket Sort +
Timsort +
Binary tree sort +"""

arr = []
length = 10000
for i in range(0, length):
    r = random.randint(0, 1000000)
    arr.append(r)
# print(arr)
start = time.monotonic()
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

    return arr


def merge(arr1, arr2):
    merged_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    merged_arr += arr1[i:]
    merged_arr += arr2[j:]

    return merged_arr


def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))
            merged_array = merge(
                arr[start:midpoint + 1], arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr
insertion_sort_arr = insertion_sort(arr)
# print(insertion_sort_arr)
print(f"Timsort {time.monotonic() - start} s.")

# Binary tree sort
start = time.monotonic()


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def inorder_traversal(root, res):
    if root:
        inorder_traversal(root.left, res)
        res.append(root.val)
        inorder_traversal(root.right, res)


def tree_sort(arr):
    root = None
    for val in arr:
        root = insert(root, val)
    res = []
    inorder_traversal(root, res)
    return res


# Приклад використання

sorted_arr_tree = tree_sort(arr)
# print(sorted_arr_tree)
print(f"Binary tree sort {time.monotonic() - start} s.")
