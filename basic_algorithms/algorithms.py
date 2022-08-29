# first solution

a = 5
b = 6
c = a + b

# print(c)

# second solution
# print(5 + 6)

# third solution
values = [5, 6]
c = sum(values)
# print(c)

# fourth solution
c = 5 + 6
# print(c)


# Represent the natural language representation of searching a list problem in code representation
list_of_numbers = [2, 3, 4, 5, 6, 90, 10, 100, 22, 45, 789, 12, 9, 78]
value = int(input('What value would you like to find? '))
for number in list_of_numbers:
    if number == value:
        c = number
        print(f'I found the value: {c}')
        break
else:
    print('value not available')

if value in list_of_numbers:
    print(f'I found the value: {value}')
else:
    print('value not available')


# # deletes an item from a list
# def delete_item(list_items, number):
#     for item in range(len(list_items)):
#         if list_items[item] == number:
#             list_items.pop(item)
#             return list_items
#     else:
#         print('item not found')
#         return list_items
#
#
# list_of_numbers = [2, 3, 4]
#
# print(delete_item(list_of_numbers, 2))


