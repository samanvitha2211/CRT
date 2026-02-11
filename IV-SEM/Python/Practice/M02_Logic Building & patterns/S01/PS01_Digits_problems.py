"""
Sample input: 1234
Sample output: 4

Sample input: 123456
Sample output: 6

Sample input: 45
Sample output: 2
"""
"""
n = int(input("Enter the number: "))
count = 0
while n>0:
    count += 1
    n = n//10
print(count)
"""
"""
print(len(str(n)))
"""
"""
n = int(input())
temp = n
s = 0
while n>0:
    s += (n%10)
    n //= 10
print(s)


print(sum(map(int,str(temp))))
"""
"""
n = int(input())
even = odd = 0
while n > 0:
    if (n%2) == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(even,odd)
"""
"""
n = int(input())
while n > 9:
    n = sum(map(int,str(n)))
print(n)
"""

