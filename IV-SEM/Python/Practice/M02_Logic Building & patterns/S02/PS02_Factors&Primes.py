'''
Read number from user and print all the factors of that number
input : 12
output : 1 2 3 4 6 12

n = int(input("Enter a number: "))
for i in range(1,n//2+1):
    if n % i == 0:
        print(i,end = ' ')
print(n)
'''

'''
No.of factors
n = int(input("Enter number"))
count = 0
for i in range(1,n//2+1):
    if n%i == 0:
        count+=1
print(count+1)
'''

'''
n = int(input("enter number: "))
count = 0
for i in range(2,n//2+1):
    if n % i == 0:
        count += 1
print("prime" if count == 0 else "not prime")
'''

'''display all the prime numbers in the given range
start = int(input())
end = int(input())
if start == 1:
    start = 2
for n in range(start,end+1):
    count = 0
    for i in range(2,n//2+1):
        if n%i == 0:
            count+=1
        if count ==0:
            print(n,end=' ')
'''

'''factorial
n = int(input("Enter number: "))
if n<0:
    print("no factorial")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
'''

