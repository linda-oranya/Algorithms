# solution 1

def indices_of_two_numbers(arr, target_sum):
    possible_sum = []
    if arr is not None and len(arr) >= 2:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target_sum:
                    possible_sum.append((i, j))
        return possible_sum
    return -1


print(indices_of_two_numbers([2, 3, 4, 5, 6, 7], 10))


