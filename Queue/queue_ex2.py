from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


def produce_binary_nums(n):
    number_queue = Queue()
    number_queue.enqueue('1')

    for i in range(n):
        front = number_queue.front()
        print(' ', front)
        number_queue.enqueue(front + '0')
        number_queue.enqueue(front + '1')

        number_queue.dequeue()


# if __name__ == '__main__':
#     produce_binary_nums(10)
