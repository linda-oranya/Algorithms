def merge_sort(list_num):
    if len(list_num) <= 1:
        return list_num
    pivot = len(list_num) // 2
    left_list = list_num[:pivot]
    right_list = list_num[pivot:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


def merge(left, right):
    merged = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            merged.append(left[0])
            left.remove(left[0])
        else:
            merged.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        merged = merged + right
    else:
        merged = merged + left
    return merged


num = [6, 2, 1, 7, 9, 3, -1, 5, 20, 15, 13, 2]
print(merge_sort(num))
