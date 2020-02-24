import math
import random

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

    operators = ['+', '-', '*', '/']
    numbers = [-5, -4, -3, -2, -1, 'x', 0, 'x', 1, 2, 3, 4, 5]

    # 1/2 x * x
    x_values = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9]
    y_values = [0, .005, .020, .045, .080, .125, .180, .245, .320, .405]

    # constructor
    def __init__(self):
        #self.tree = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
        self.tree = self.genTree()
        self.expression = []
        self.evalStack = Stack()
        #evaluates the tree expression
        inorder(self.tree, self.evalStack)
        print(self.evalStack.stack)
        #once stack reaches lenght 3, we will evaluate that expression
        #
        

        #randomly generate strings of expressions and just put them in stacks and do it all based on that alone
        #for crossover and/or mutation, make a separate array for the indeces of the operators in a chromosome's
        #expression. This way, we can guarantee a subtree from random picking.

    
    def eval(self):
        while not self.evalStack.isEmpty():
            n1 = self.evalStack.pop()
            if n1 == 'x':
                pass
            elif n1 > -6 or n1 < 6:
                pass
            else:
                pass

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

        flag = True
        while flag:
            # randomly pick between an operator and a number for each node,
            # then pick its leaf nodes? (increment a var that'll keep track of num of parent nodes)
            # stop generating at terminal (number) values
            # so any number becomes a leaf -- will never be a parent
            # an operator will always be a parent node
            pass

        
        return
    def evalFitness(self):
        return
    def crossover(self, oExpression):
        return
    def mutate(self):
        return 

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

def inorder(a, stack, i=0):
    if i >= len(a):
        return
    l, r = childrenNodesIndeces(i)
    inorder(a, stack, r)
    if str(a[i]) != "None":
        stack.push(a[i])
       #print(a[i])
    inorder(a, stack, l)

    


###
def main():
    populationSize = 600
    population = []
    a = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
    for i in range(0, 1):
        population.append(Chromosome())
    #traversed(population[0].tree)
    #inorder(population[0].tree)

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
