class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add the data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            # add the data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # visit the base node
        elements.append(self.data)
        # visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order(self):
        elements = []

        # visit the left tree
        if self.left:
            elements += self.left.post_order()
        # visit the right tree
        if self.right:
            elements += self.right.post_order()
        # visit the base node
        elements.append(self.data)

        return elements

    def pre_order(self):
        elements = []
        # visit the base node
        elements.append(self.data)
        # visit the left tree
        if self.left:
            elements += self.left.pre_order()
        # visit the right tree
        if self.right:
            elements += self.right.pre_order()

        return elements

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            # val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        # elements = []
        # elements = self.in_order_traversal()
        # return elements[0]
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        # elements = []
        # elements = self.in_order_traversal()
        # return elements[-1]
        if self.right:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        # total = 0
        # elements = []
        # elements = self.in_order_traversal()
        # for i in range(len(elements)):
        #     total += elements[i]
        # return total
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # if the left subtree

            min_val = self.left.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

            # if the right subtree
            max_val = self.right.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)


def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [15, 12, 7, 14, 27, 20, 88, 23]
    numbers_list = build_tree(numbers)
    # print(f'IN ORDER: {numbers_list.in_order_traversal()}')
    # print(numbers_list.search(30))
    # print(f'MIN VALUE: {numbers_list.find_min()}')
    # print(f'MAX VALUE: {numbers_list.find_max()}')
    # print(f'POST ORDER: {numbers_list.post_order()}')
    # print(f'PRE ORDER: {numbers_list.pre_order()}')
    # print(f'Total: {numbers_list.calculate_sum()}')
    print()
