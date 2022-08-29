# [0, 1, 0, 3, 12]

def remove_zeroes(arr):
    for i in arr:
        if 0 in arr:
            arr.remove(0)
            arr.append(0)
    return arr


print(remove_zeroes([0, 1, 0, 3, 12]))


def move_zeros(nums: list[int]) -> list[int]:
    return [ch for ch in nums if ch != 0] + [0 for _ in range(nums.count(0))]