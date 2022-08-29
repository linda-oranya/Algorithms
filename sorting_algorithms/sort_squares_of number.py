from bubble_sort import sort_bubble
from merge_sort import merge_sort


def first_solution_sort(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * numbers[i]
    numbers.sort()
    return numbers


def second_solution_sort(numbers):
    list_numbers = merge_sort(numbers)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2
    return list_numbers


list_numbers = [6, 2, 1, 7, 9, 3, -1, 5, 20, 15, 13, 2]

print("merge sort", merge_sort(list_numbers))
print("first_solution", first_solution_sort(list_numbers))
print("second_solution", second_solution_sort(list_numbers))
