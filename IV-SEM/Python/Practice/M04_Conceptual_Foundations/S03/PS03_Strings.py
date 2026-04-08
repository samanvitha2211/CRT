'''
s = "python programming"
print(s.capitalize())
print(s.title())
s = s.title()
print(s)
print(s.replace("on", "ON"))
print(s)
'''

'''
#Reverse a string without using built-in functions and slicing
#input = "abc" ==> output = "cba"
def reverse_string(s):
    stop = -1 * (len(s) + 1)
    res = ""
    for i in range(-1, stop, -1):
        res += s[i]
    return res
print(reverse_string("abc"))
'''
'''
#Reverse a string using slicing
def reverse_string(s):
    return s[::-1]
print(reverse_string("abc"))

#Reverse a string using built-in functions
def reverse_string(s):
    return "".join(reversed(s))
print(reverse_string("abc"))


#check if a string is a palindrome
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("Samanvitha "))


def Reverse_String(s):
    res = ""
    for ch in s:
        res = ch + res
    return res

def is_palindrome(s):
    return Reverse_String(s) == s
print(is_palindrome("Samanvitha "))
'''




