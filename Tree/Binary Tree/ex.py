class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def cal_sum(self):
        left_sum = self.left.cal_sum() if self.left else 0
        right_sum = self.right.cal_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [15, 4, 1 , 20, 9, 23, 18, 17, 19, 22]
    number_list = build_tree(numbers)
    # print(number_list.in_order_traversal())
    # print(number_list.pre_order_traversal())
    # print(number_list.post_order_traversal())
    # print(number_list.search(3))
    # print(number_list.cal_sum())
    # print(number_list.find_min())
    # print(number_list.find_max())
    print(f'Sorted List: {number_list.in_order_traversal()}')
    # number_list.delete(34)
    # print('After deleting 34: ', number_list.in_order_traversal())
    # number_list.delete(18)
    # print('After deleting 18: ', number_list.in_order_traversal())
    # number_list.delete(23)
    # print('After deleting 23: ', number_list.in_order_traversal())
    # number_list.delete(20)
    # print('After deleting 20: ', number_list.in_order_traversal())
    number_list.delete(20)
    print('After deleting 20 : ', number_list.in_order_traversal())

