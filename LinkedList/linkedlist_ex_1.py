# doubly linkedlist
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedlist:
    def __init__(self):
        self.head = None

    # insert the node from the begining the linked list

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    # print forward
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = " "

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    # print backward
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        print(llstr)

    # get the last node
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    # insert the node at the end of the linked list
    def insert_at_last(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

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
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
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
                node = Node(data, itr.next,itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

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


if __name__== '__main__':

    ll = DoublyLinkedlist()
    ll.insert_value(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_last("figs")
    ll.print_forward()
    ll.insert_at(0, "apple")
    ll.print_forward()
    ll.print_backward()
    print(ll.get_length())
    ll.insert_at(5,"papaya")
    ll.print_forward()
    print(ll.get_length())
    ll.insert_at(6, "jackfruit")
    ll.print_forward()

