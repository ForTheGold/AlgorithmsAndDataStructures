class Tree:
    def __init__(self, key, parent=None, left=None, right=None):
        self.parent = parent
        self.key = key
        self.left = left
        self.right = right

    def insert(self, data):
        if self.key:
            if data < self.key:
                if self.left is None:
                    self.left = Tree(data)
                    self.left.parent = self.key
                else:
                    self.left.insert(data)
            elif data > self.key:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.key = data
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.key)
        if self.right:
            self.right.print_tree()

    def find_value(self, value):
        if value == self.key:
            return True
        if value < self.key:
            if self.left is None:
                return False
            else:
                return self.left.find_value(value)
        if value > self.key:
            if self.right is None:
                return False
            else:
                return self.right.find_value(value)
    
    #def delete_value(self, value):
        

tree = Tree(5)
tree.insert(3)
tree.insert(10)
tree.insert(4)
tree.insert(1)
tree.insert(6)
tree.insert(2)
tree.print_tree()
print(tree.find_value(3))
print(tree.find_value(20))
print(tree.find_value(2))
print(tree.find_value(100))
