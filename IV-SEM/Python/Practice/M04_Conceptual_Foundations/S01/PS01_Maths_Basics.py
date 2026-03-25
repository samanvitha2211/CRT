'''#1. find the GCD
#solution 1
a = int(input())
b = int(input())
min_val = min(a, b)
for i in range(1,min_val+1):
    if a%i == 0 and b%i == 0:
        gcd = i
print(gcd)

#solution 2
import math
print(math.gcd(a, b))

#solution 3
while b!= 0:
    a, b = b, a % b
print(a)

''' 


#2. find the LCM
#solution 1
a = int(input())
b = int(input())
x,y = a, b
while y!= 0:
    x, y = y, x % y
gcd = x
lcm = (a*b)//gcd
print(lcm)

#solution 2
import math 
print((a*b)//math.gcd(a, b))


