from heapq import heappush, heappop
import random


def heapsort(list_of_numbers):
    h = []
    for value in list_of_numbers:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]


random_list = random.sample(range(100), 10)

print(random_list)
print(heapsort(random_list))
