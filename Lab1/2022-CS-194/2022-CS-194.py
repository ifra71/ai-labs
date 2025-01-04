#Q1
def cube(number):
    if isinstance(number, (int, float)): 
        return number**3
    else :
        return "Enter a valid input "
number=int(input("enter a number to get its cube : "))
print(cube(number))


def factorial(n):
    if n<0:
        return "Enter a positive number "
    else:
          fact=1
          for i in range(1,n+1):
              fact=fact*i
          return fact
n=int(input("enter a number to take factorial : "))
print(factorial(n))


def findAlphabeticallyLastWord(string):
        words=string.split();
        sort=sorted(words, key=str.lower)
        return sort[-1]
string=input("enter a sentebce : ")
print(findAlphabeticallyLastWord(string))


def count_pattern(pattern, lst):
    number = 0
    lengthOfPattern = len(pattern)
    lengthOfList = len(lst)    
    for i in range(lengthOfList - lengthOfPattern + 1):
        if tuple(lst[i:i + lengthOfPattern]) == pattern:
            number += 1   
    return number


#Q2
def depth(expr):
    if not isinstance(expr, (list, tuple)):
        return 0
    return 1 + max(depth(item) for item in expr)

print("tthe depth is :", depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1), ('/', 5, 2)))))


#Q3
def tree_ref(tree, indices):
    if not indices:
        return tree
    if not isinstance(tree, (tuple, list)):
        return "The tree structure should be a tuple or list."
    if not 0 <= indices[0] < len(tree):
       return "Index out of range."
    return tree_ref(tree[indices[0]], indices[1:])

tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))

print("tree refernce :  " , tree_ref(tree, (3, 1)))  


#Q4

def do_multiply(expr1, expr2):
    if isinstance(expr1, Sum) and isinstance(expr2, Sum):
        result = []
        for term1 in expr1:
            for term2 in expr2:
                result.append(multiply(term1, term2))
        return Sum(result).simplify()
    
    elif isinstance(expr1, Sum) and isinstance(expr2, Product):
        result = []
        for term1 in expr1:
            result.append(multiply(term1, expr2))
        return Sum(result).simplify()
    
    elif isinstance(expr1, Product) and isinstance(expr2, Sum):
        result = []
        for factor in expr1:
            result.append(multiply(factor, expr2))
        return Sum(result).simplify()
    
    elif isinstance(expr1, Product) and isinstance(expr2, Product):
        return Product(expr1 + expr2).simplify()
    
    else:
        return Product([expr1, expr2]).simplify()

    raise NotImplementedError
