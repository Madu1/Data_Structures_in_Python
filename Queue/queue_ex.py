import time
from collections import deque
import threading


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print('Queue is empty..')
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


food_ordering_queue = Queue()


def place_order(orders):
    for order in orders:
        print('Placing order for :', order)
        food_ordering_queue.enqueue(order)
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        order = food_ordering_queue.dequeue()
        print('Now serving: ', order)
        time.sleep(2)


# if __name__ == '__main__':
#     food_queue = ['samosa', 'biryani', 'burger', 'lime juice', 'fried rice']
#
#     t1 = threading.Thread(target=place_order, args=(food_queue,))
#     t2 = threading.Thread(target=serve_order)
#
#     t1.start()
#     t2.start()


