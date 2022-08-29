[1, 2, -2, 10, 3]


# iterative_method
def find_peak(arr):
    peak_index = 0
    for i in range(len(arr)):  # [1, 2, -2, 10, 3] , length = 5, i = 0, 1 = 1, i = 2, i = 3, i = 4
        if arr[i] > arr[peak_index]:  # 3 > 2
            peak_index = i
    return peak_index


# binary approach
def find_peak_binary_search(arr):
    left = 0
    right = len(arr) - 1
    while left < right:  # 0, 4
        mid = (left + right) // 2  # 2
        if arr[mid] < arr[mid + 1]:  # arr[2] < arr[3]
            left = mid + 1    # 3
        else:
            right = mid
    return left


print(find_peak_binary_search([1, 200, 5, 3, 4, 100, 9]))
