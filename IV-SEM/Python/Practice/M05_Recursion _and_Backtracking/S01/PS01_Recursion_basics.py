'''
def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)
print(natural_sum(5))
print(natural_sum(10))

def natural_sum_iterative(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res
print(natural_sum_iterative(5))
print(natural_sum_iterative(10))


def natural_sum(n):
    s = 0
    for i in range(n, 0, -1):
        s += i
    return s
print(natural_sum(5))
print(natural_sum(10))
'''
 
''''
def factorial(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s
print(factorial(5)) 

def factorial(n):
    if n<0:
        return "Factorial doesnot exist for -ve"
    elif n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))     
print(factorial(4))
'''
''' 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))

'''

def GCD(a,b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
print(GCD(48, 18))