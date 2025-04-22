def find_sort(arr):
    smalest = arr[0]
    smalest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smalest:
            smalest = arr[i]
            smalest_index = i
    return smalest_index


def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smalest = find_sort(arr)
        new_arr.append(arr.pop(smalest))
    return new_arr


print(selection_sort([1, 5, 4, 3, 2, 9, 7]))
