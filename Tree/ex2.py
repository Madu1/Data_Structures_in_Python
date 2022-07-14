class TreeNode:
    def __init__(self, data):
        self.data = data
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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' '*self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_location_tree():
    root = TreeNode('Global')

    india = TreeNode('India')

    gujarat = TreeNode('Gujarat')
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

    karnatak = TreeNode('Karnataka')
    karnatak.add_child(TreeNode('Bangluru'))
    karnatak.add_child(TreeNode('Mysor'))

    usa = TreeNode('USA')
    new_j = TreeNode('New Jersey')
    new_j.add_child(TreeNode('Princeton'))
    new_j.add_child(TreeNode('Trenton'))

    cal = TreeNode('California')
    cal.add_child(TreeNode('San francisco'))
    cal.add_child(TreeNode('Mountain View'))
    cal.add_child(TreeNode('Palo Alto'))

    india.add_child(gujarat)
    india.add_child(karnatak)
    usa.add_child(new_j)
    usa.add_child(cal)
    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(1)