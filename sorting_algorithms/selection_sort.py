def sort_by_selection(list_of_numbers):
    for i in range(len(list_of_numbers) - 1):
        min_value = i
        for j in range(i, len(list_of_numbers)):
            if list_of_numbers[j] < list_of_numbers[min_value]:
                min_value = j
        temp = list_of_numbers[i]
        list_of_numbers[i] = list_of_numbers[min_value]
        list_of_numbers[min_value] = temp
    return list_of_numbers


list_num = [6, 2, 1, 7, 9, 3]
print(sort_by_selection(list_num))
