import math
from random import randint

# Brian Spencer
# CSC 320
# Assignment 2: find the equation of a line given inputs and outputs of that function, genetically. 

class Stack:
    def __init__(self):
        self.stack = []
        self.len = len(self.stack)

    def push(self, value):
        self.stack.append(value)
        self.len = self.len + 1

    def pop(self):
        if not self.isEmpty():
            x = self.stack.pop()
            self.len = self.len - 1
        return x

    def remove(self):
        if not self.isEmpty():
            self.stack.pop()
            self.len = self.len - 1

    def top(self):
        return self.stack[self.len-1]

    def isEmpty(self):
        return self.len == 0

class Chromosome:



    # constructor
    def __init__(self):
        #self.tree = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
        self.tree = []
        self.expression = []
        self.exp = ""
        self.evalStack = Stack()
        #evaluates the tree expression
        #inorder(self.tree, self.evalStack)
        #print(self.evalStack.stack)
        #print(self.evalStack.stack)
        #once stack reaches lenght 3, we will evaluate that expression
        #
        self.operators = ['+', '-', '*', '/']
        self.numbers = [-5, -4, -3, -2, -1, 'x', 'x', 1, 2, 3, 4, 5]

        # 1/2 x * x
        self.x_values = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9]
        self.y_values = [0, .005, .020, .045, .080, .125, .180, .245, .320, .405]
        self.genTree()
        self.inorder(self.tree)
        self.evalFitness()

        #randomly generate strings of expressions and just put them in stacks and do it all based on that alone
        #for crossover and/or mutation, make a separate array for the indeces of the operators in a chromosome's
        #expression. This way, we can guarantee a subtree from random picking.

    def inorder(self, a, i=0):
        if i >= len(a):
            return
        l, r = childrenNodesIndeces(i)
        self.inorder(a, r)
        if str(a[i]) != "None":
            self.exp = self.exp + str(a[i])
        self.inorder(a, l)

    def eval(self, val):
        oper = ''
        op1 = -6
        op2 = -6
        value = 0
        for i in range(0, len(self.exp)):
            element = self.exp[i]
            if isOp(element):
                oper = element
            elif op1 == -6:
                if element == 'x':
                    op1 = val
                else:
                    op1 = int(element)
            elif op2 == -6:
                if element == 'x':
                    op2 = val
                else:
                    op2 = int(element)
                value = self.doOp(op1, op2, oper)
                op1 = -6
                op2 = -6
        return value

    def doOp(self, n1, n2, op):
        print('n1: ',n1)
        print('n2: ',n2)
        print('op: ',op)
        n1 = int(n1)
        n2 = int(n2)
        if op == '+':
            return n1 + n2
        elif op == '-':
            return n1 - n2
        elif op == '*':
            return n1 * n2
        else:
            return n1 / n2



    def genTree(self):
        #values between -5 and 5 or x (except 0?).
        #all foru basic operands (+, -, *, /)
        #includes the None values for the tree
        """
                 1
              *
                 3
           -
                 None
              5
                 None
        /
                 None
              2
                 None
           +
                 None
              1
                 None

        ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]

        1+2/5-1*3
        """
        i = 0
        r = randint(0,1)
        if r == 0:
            t = randint(0, len(self.operators)-1)
            self.tree.append(self.operators[t])
        else:
            t = randint(0, len(self.numbers) - 1)
            self.tree.append(self.numbers[t])
        i += 1
        eqLength = len(self.tree)
        while i < eqLength + 2:
            # randomly pick between an operator and a number for each node,
            # then pick its leaf nodes? (increment a var that'll keep track of num of parent nodes)
            # stop generating at terminal (number) values
            # so any number becomes a leaf -- will never be a parent
            # an operator will always be a parent node
            r = randint(0,1)

            parent = findOpParent(i, len(self.tree))

            #['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]

            if r == 0:
                t = randint(0, len(self.operators)-1)
                if isOp(self.tree[parent]):
                    #if isOp(self.tree[i-1]):
                    self.tree.append(self.operators[t])
                elif not isNone(self.tree[parent]):
                    self.tree.append(None)
            else:
                t = randint(0, len(self.numbers) - 1)
                if not isOp(self.tree[parent]):
                    if not isNone(self.tree[parent]):
                        self.tree.append(None)
                else:
                    self.tree.append(self.numbers[t])
            i += 1
            eqLength = len(self.tree)
        print(self.tree)

        
        return
    def evalFitness(self):
        fitness = 0
        for i in range(len(self.x_values)):
            fitness += self.eval(self.x_values[i]) - self.y_values[i]
        print(fitness**2)
        return fitness**2
    def crossover(self, oExpression):
        return
    def mutate(self):
        return 

def findOpParent(c, len):
    for i in range(0, len):
        l, r = childrenNodesIndeces(i)
        """
        if c == r:
            return i, "right child"
        else:
            return i, "left child"
        """
        if c == l or c == r:
            return i
    return -1
def isOp(e):
    if e == '+' or e == '-' or e == '*' or e == '/':
        return True
    return False
def isNone(e):
    if str(e) == "None":
        return True
    return False

def childrenNodesIndeces(i):
    return (2 * i) + 1, (2 * i) + 2


def traversed(a, i=0, d=0):
    if i >= len(a):
        return
    l, r = childrenNodesIndeces(i)
    traversed(a, r, d=d + 1)
    if not str(a[i]) == "None":
        print("   " * d + str(a[i]))
    traversed(a, l, d=d + 1)
    


###
def main():
    populationSize = 600
    population = []
    a = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
    for i in range(0, 2):
        population.append(Chromosome())

if __name__ == "__main__":
    main()

"""
         1
      *
         3
   -
      5
/
      2
   +
      1
      
(1+2)/(5-(1*3))

1+2/5-1*3
"""
