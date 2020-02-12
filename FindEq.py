class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        if data == '+' or data == '-' or data == '*' or data == '/':
            self.value = float('inf')
            self.type = 'op'
        else:
            self.value = data
            self.type = 'num'

    def insert(self, data, typ):
        if self.data and typ == 'num':
            if self.type == 'num':
                if data < self.value:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                elif data > self.value:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.right = Node(data)
        elif self.data and typ = 'op':
            if self.type == 'op':
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.right = Node(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data
            self.type = typ
            
    def eval(root): 
        if root is None: 
            return 0
        if root.left is None and root.right is None: 
            return int(root.data) 
        left_sum = evaluateExpressionTree(root.left) 
        right_sum = evaluateExpressionTree(root.right)
        
        if root.data == '+': 
            return left_sum + right_sum
        
        elif root.data == '-': 
            return left_sum - right_sum 
          
        elif root.data == '*': 
            return left_sum * right_sum 
          
        else: 
            return left_sum / right_sum

        


if __name__ == '__main__':
    root = Node('+')
    root.insert(6, 'num')
    root.insert('-', 'op')
    root.insert(3, 'num')
    root.insert(2, 'num')

    #root.eval()
    #https://medium.com/swlh/build-binary-expression-tree-in-python-36c04123e57b
    #https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm

### equally important consideration for tree
    
def childNodes(i):
     return (2*i)+1, (2*i)+2

def traversed(a, i=0, d = 0):
    if i >= len(a):
        return 
    l, r =  childNodes(i)
    traversed(a, r, d = d+1)
    print("   "*d + str(a[i]))
    traversed(a, l, d = d+1)

a =  ['+', 6, '-', None, None, 12, 3]

traversed(a)

###
