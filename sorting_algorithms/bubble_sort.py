def sort_bubble(list_num):
    for i in range(len(list_num) - 1, 0, -1):
        for j in range(i):
            if list_num[j] > list_num[j + 1]:
                temp = list_num[j]
                list_num[j] = list_num[j + 1]
                list_num[j + 1] = temp
    return list_num


# list_num = [6, 2, 1, 7, 9, 3, -1, 5, 20, 15, 13, 2]
# print(sort_bubble(list_num))
