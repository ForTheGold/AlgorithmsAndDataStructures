class Node:
    def __init__(self, value, parent=None, left=None, right=None):
        self.parent = parent
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self, value):
        root = Node(value)
        self.root = root

    def insert(self, value):
        node = Node(value)
        prev = None
        curr = self.root

        while curr != None:
            prev = curr
            if node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        
        node.parent = prev

        if prev == None:
            self.root = prev
        elif node.value < prev.value:
            prev.left = node
        elif node.value > prev.value:
            prev.right = node

    def find_min(self, node=None):
        if not node:
            node = self.root
        curr = node
        while curr.left:
            curr = curr.left
        return curr.value
    
    def find_max(self, node=None):
        if not node:
            node = self.root
        curr = node
        while curr.right:
            curr = curr.right
        return curr.value

    def find_tree_successor(self, value):
        node = self.find_node(value)
        if node.right:
            return self.find_min(node.right)
        parent = node.parent
        while parent and node == parent.right:
            node = parent
            parent = parent.parent
        if parent:
            return parent.value
        return parent

    def find_value_recur(self, node, value):
        if not node:
            return node
        if node.value == value:
            return node.value
        if value < node.value:
            return self.find_value_recur(node.left, value)
        else:
            return self.find_value_recur(node.right, value)

    def find_value_iter(self, value):
        curr = self.root
        while curr and value != curr.value:
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        if curr:
            return curr.value
        return curr

    def find_node(self, value):
        curr = self.root
        while curr and value != curr.value:
            if value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def transplant_node(self, node_one, node_two):
        if not node_one.parents:
            self.root = node_two
        elif node_one = node_one.parent.left:
            node_one.parent.left = node_two
        else:
            node_one.parent.right = node_two
        if node_two:
            node_two.parent = node_one.parent

    
    def print_tree_recur(self, node):
        if node != None:
            self.print_tree_recur(node.left)
            print(node.value)
            self.print_tree_recur(node.right)

    def print_tree_iter(self, tree):
        stack = []
        current = tree.root

        while True:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.value)
                current = current.right
            else:
                break


tree = Tree(5)
tree.insert(1)
tree.insert(4)
tree.insert(10)
tree.insert(2)
tree.insert(8)
tree.insert(3)
tree.print_tree_recur(tree.root)
print("-" * 10)
tree.print_tree_iter(tree)
print("-" * 10)
print(tree.find_value_recur(tree.root, 10))
print(tree.find_value_recur(tree.root, 100))
print(tree.find_value_recur(tree.root, 0))
print(tree.find_value_recur(tree.root, 8))
print(tree.find_value_recur(tree.root, 5))
print("-" * 10)
print(tree.find_value_iter(100))
print(tree.find_value_iter(0))
print(tree.find_value_iter(10))
print(tree.find_value_iter(8))
print(tree.find_value_iter(5))
print("-" * 10)
print(tree.find_min())
print(tree.find_max())
print("-" * 10)
print(tree.find_tree_successor(10))
print(tree.find_tree_successor(8))
print(tree.find_tree_successor(5))
print(tree.find_tree_successor(3))
print(tree.find_tree_successor(1))