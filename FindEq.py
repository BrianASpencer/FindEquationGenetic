class Chromosome:

    operators = ['+', '-', '*', '/']
    numbers = [-5, -4, -3, -2, -1, 0, 'x', 1, 2, 3, 4, 5]

    # constructor
    def __init__(self):
        self.tree = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
        self.expression = []

def childNodes(i):
    return (2 * i) + 1, (2 * i) + 2


def traversed(a, i=0, d=0):
    if i >= len(a):
        return
    l, r = childNodes(i)
    traversed(a, r, d=d + 1)
    if not str(a[i]) == "None":
        print("   " * d + str(a[i]))
    traversed(a, l, d=d + 1)

def inorder(a, i=0):
    if i >= len(a):
        return
    l, r = childNodes(i)
    inorder(a, r)
    if str(a[i]) != "None":
        print(str(a[i]))
    inorder(a, l)

def eval(a, i=0):
    if a[i] is None:
        return 0
    l, r = childNodes(i)
    if l is None and r is None:
        return int(a[i])

    print(i)

    left_sum = eval(a, l)
    right_sum = eval(a, r)

    if a[i] == '+':
        return left_sum + right_sum
    elif a[i] == '-':
        return left_sum - right_sum
    elif a[i] == '*':
        return left_sum * right_sum
    elif a[i] == '/':
        return left_sum / right_sum


###
def main():
    populationSize = 600
    population = []
    a = ['/', '+', '-', 1, 2, 5, '*', None, None, None, None, None, None, 3, 1]
    for i in range(0, 1):
        population.append(Chromosome())
    traversed(population[0].tree)
    inorder(population[0].tree)

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
