def sort_by_insertion(list_num):
    for i in range(1, len(list_num)):
        j = i-1
        next_value = list_num[i]
        while (list_num[j] > next_value) and (j >= 0):
            list_num[j+1] = list_num[j]
            j = j-1
            list_num[j+1] = next_value
    return list_num


list_num = [6, 2, 1, 7, 9, 3, -1, 5, 20, 15, 13, 2]
print(sort_by_insertion(list_num))