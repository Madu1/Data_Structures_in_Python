class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # insert the node from the begining the linked list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # print the linked list
    def print(self):
        if self.head is None:
            print("Linkedlist is null.")
            return

        itr = self.head
        llstr = ' '
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    # insert the node at the end of the linked list
    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    # insert values as list to the linked list
    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_last(data)

    # get the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # remove element at a given index

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # insert index into anywhere of the linked list

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # insert_after_values

    def insert_after_values(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    # remove by value

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    '''ll.insert_at_begining(5)
    ll.insert_at_begining(10)
    ll.insert_at_begining(25)
    ll.insert_at_begining(89)
    for i in range(10):
        ll.insert_at_begining(i)'''
    '''ll.insert_at_last(5)
    ll.insert_at_last(8)
    ll.insert_at_last(25)
    ll.insert_at_last(95)'''

    # ll.insert_value(['banana', 'mango', 'grapes', 'apple'])
    ll.insert_value([23, 65, 15, 69, 12, 10, 3, 89])

    ll.print()
    ''' ll.insert_at(2,45)
    ll.insert_at(0, 67)
    ll.remove_at(5)'''
    ll.insert_after_values(65, 100)
    ll.print()
