"""
li = [1,2,3,4,5]
output = [2,4,6,8,10]

li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i*2)
print(res)
#or
print([i*2 for i in li])
"""


'''
li = [1,2,3,4,5]
#output : [2,4]
res = []
for i in li:
    if i%2==0:
        res.append(i)
print(res)
#or
print([i for i in li if i%2==0])
'''

'''
#['a','b','c'] ==>"abc"
li1 = ['a','b','c']
res = ""
for ch in li1:
    res += ch
print(res)
#or
print("".join(li1))
'''


'''
n=4
output: 
   *
  * *
 * * *
* * * *

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''

'''
2.Inverted pyramid

n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
'''

'''
3.Diamond
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
'''

'''
4. number pyramid
output:
     1
    1 2
   1 2 3
  1 2 3 4
  
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+" ".join(str(x) for x in range(1,i+1)))
'''


#5. Alphabetical pattern
n = int(input())
ch = 65
for i in range(n):
    for j in range(i+1):
        print(chr(ch),end = " ")
        ch +=1
    print()
