from collections import deque


queue = deque()
queue.append('first')
queue.append(2)
queue.append('11')
queue.append('ok')

queue.popleft()

print(queue)