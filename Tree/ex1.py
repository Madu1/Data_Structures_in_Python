class TreeNode:
    request = input(
        'Please enter what do you want to display (N) for Name, (D) for Designation and (B) for Both: ').upper()

    def __init__(self, name, desg):
        self.name = name
        self.desg = desg
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''

        if TreeNode.request == 'N':
            print(prefix + self.name)
        if TreeNode.request == 'D':
            print(prefix + self.desg)
        if TreeNode.request == 'B':
            print(prefix + self.name, f'({self.desg})')
        if self.children:
            for child in self.children:
                child.print_tree()


def build_employee_tree():
    root = TreeNode("Nilupul", 'CEO')

    cto = TreeNode('Chinmay', 'CTO')

    ifh = TreeNode('Vishwa', 'Infrastructure Head')
    ifh.add_child(TreeNode('Dhaval', 'Cloud Manager'))
    ifh.add_child(TreeNode('Abhijit', 'App Manager'))

    application_head = TreeNode('Aamir', 'Application Head')

    hr = TreeNode('Gels', 'HR Head')
    hr.add_child(TreeNode('Peter', 'Recruitment Manager'))
    hr.add_child(TreeNode('Waqas', 'Policy Manager'))

    cto.add_child(ifh)
    # cto.add_child(hr)
    cto.add_child(application_head)
    root.add_child(cto)
    root.add_child(hr)
    return root


if __name__ == '__main__':
    root = build_employee_tree()
    root.print_tree()
