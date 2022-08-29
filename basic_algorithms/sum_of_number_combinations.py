def sum_of_combinations(i, n, output, index):
    if n == 0:
        print(output[:index])
    for j in range(i, n + 1):
        output[index] = j
        sum_of_combinations(j, n - j, output, index + 1)


n = 5
output = [None] * n

print(sum_of_combinations(1, n, output, 0))
