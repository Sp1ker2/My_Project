def binars(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return low
        elif guess > item:
            high = mid - 1
            return high
        else:
            low = mid + 1


my_list = [1, 3, 5, 7, 9, 12, 34, 231, 345]
print(binars(my_list, 3))
