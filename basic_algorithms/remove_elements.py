def remove_all_occurrence_of_values(values, x):
    new_list = []
    for j in values:
        if j != x:
            new_list.append(j)

    return new_list


print(remove_all_occurrence_of_values([1, 3, '4', 5, 5, 6, 9, 2], '4'))

# [1, 2, 3, 4, 5]
# O(1)

# f(x) = log n + 3n
# O(n)


