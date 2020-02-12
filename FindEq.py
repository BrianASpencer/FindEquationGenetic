class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        if data == '+' or data == '-' or data == '*' or data == '/':
            self.value = float('inf')
        else:
            self.value = data

    def insert(self, data):
        if self.data:
            if data < self.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

if __name__ == '__main__':
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)

    root.PrintTree()
    #https://medium.com/swlh/build-binary-expression-tree-in-python-36c04123e57b
