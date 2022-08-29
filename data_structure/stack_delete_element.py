import random


def delete_smaller_element(arr, k):
    stack = []
    stack.append(arr[0])
    count = 0
    for i in range(len(arr)):
        while (len(stack) != 0) and count < k and stack[0] < arr[i]:
            stack.pop()
            count += 1
        stack.append(arr[i])
    return stack


N = random.sample(range(10), 10)

print(N)
print(delete_smaller_element(N, 10))
