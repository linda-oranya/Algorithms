def find_element(nums, target):  # iterative approach
    initial = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if initial == -1:
                initial = i
                last = i
            else:
                last = i
    return [initial, last]


def find_element_binary(nums, target):  # [1, 1, 1, 5, 6, 9, 10, 15, 19, 91], 1
    min_index = 0  # 0
    max_index = len(nums) - 1  # 9
    initial = -1  # 0
    while min_index <= max_index:   # 0 <= -1
        mid = (min_index + max_index) // 2  # 0
        if nums[mid] == target:  # yes
            initial = mid
            max_index = mid - 1
        elif nums[mid] > target:  # 6 > 1
            max_index = mid - 1   # 4 - 1
        else:
            min_index = mid + 1

    min_index = 0
    max_index = len(nums) - 1
    last = -1
    while min_index <= max_index:
        mid = (min_index + max_index) // 2
        if nums[mid] == target:
            last = mid
            min_index = mid + 1
        elif nums[mid] > target:
            max_index = mid - 1
        else:
            min_index = mid + 1
    return [initial, last]


sorted_list = [1, 1, 1, 5, 6, 9, 10, 15, 19, 91]

random_list = [1, 200, 5, 3, 4, 100, 9]

#print(find_element_binary(sorted_list, 91))


import bisect
bisect.insort(random_list, 10)
print(random_list)


