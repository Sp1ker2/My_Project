# def sum (arr):
#     total = 0
#     for x in arr:
#         print(x)
#         total +=x
#         # print(x)
#     return total
# print(sum([1,2,3,4]))


def rec(arr):
    if arr == []:
        return 0
    else:
        return 1 + rec(arr[2:])


print(rec([1, 2, 3, 4]))
