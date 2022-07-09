from collections import deque
from queue import Queue

# Implement queue by using list
#
# queue = []
# queue.append('a')
# queue.append('b')
# queue.append('c')
#
# print(queue)
#
# queue.pop()
# queue.pop()
# print(queue)


# Implement a queue by using deque

# que = deque()
# que.append('a')
# que.append('b')
# que.append('c')
#
# print(que)
# print(que.popleft())
# print(que)

# Implement a queue by Queue class
# initialize the maximum size of the queue

q = Queue(maxsize=3)
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')

print(q.qsize())
print('\nFUll:', q.full())
# q.put('d')
# print(q)
# print(q.get())
# print(q.get_nowait())
print('\nEmpty:', q.empty())
print(q.get())
print(q.get())
print(q.get())
print('\nEmpty:', q.empty())


