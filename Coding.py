print("--------------Program 1-------------------")
#Implement Plaindrome using Iterator
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
	        return False
        return True

# main function
s = "kayak"
ans = isPalindrome(s)

if (ans):
	print("Yes")

else:
	print("No")

#Implement Plaindrome using Generator
def palin_generator():
    """Generates palindromic numbers."""

    palindromes=[]

    for count in range(100):
        n = str(count)
        if n == n[::-1]:
            palindromes.append(n)
    print(palindromes)
print(palin_generator())

print("--------------Program 2-------------------")
#2)Sum of 2 digits into output

def sum_of_digit(num1,num2):
   return int(num1)+int(num2)

num1 = list(str(int(input("Enter first number : "))))
num2 = list(str(int(input("Enter second number : "))))
res = list(map(sum_of_digit,num1,num2))
temp=0
for i in res:
   temp = temp+i
print("Final output : ",temp)

#3) Reverse string without symbols
print("--------------Program 3-------------------")
def reverse_string(st):
    return ' '.join(reverse_word(word) for word in st.split())

def reverse_word(st):
    stack = []
    for el in st:
        if el.isalpha():
            stack.append(el)
    result = ''
    for el in st:
        if el.isalpha():
            result += stack.pop()
        else:
            result += el
    return result

instr = 'fe@#dc!ba'

print(reverse_string(instr))


print("--------------Program 4-------------------")
from collections import Counter
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
counts = dict(Counter(some_list))
duplicates = {key:value for key, value in counts.items() if value > 1}
print(duplicates)

print("--------------Program 5-------------------")
print('_'*20, "5. ---------------", '_' * 20)
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
   if isinstance(t, int):
       for i in t2:
           if i not in lis2 and isinstance(i, int):
               lis2.append(i)
               lis1.append((t + i))
               break
   else:
       for i in t2:
           if i not in lis2 and isinstance(i, str):
               lis2.append(i)
               lis1.append((t + i))
               break

print(lis1)



print("--------------Program 6-------------------")
print(" ------Write a Python program to remove leading zeros from an IP address.-----")
def remove_zero_from_ip(ip_add):
    new_ip_add=".".join([str(int(i))for i in ip_add.split(".")])
    return new_ip_add;
print(remove_zero_from_ip("216.08.094.196"))


print("--------------Program 7-------------------")
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output = []
# function used for removing nested
# lists in python using recursion
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)
# Driver code
print('The original list: ', l)
reemovNestings(l)
print('The list after removing nesting: ', output)

print("--------------Program 8-------------------")

with open(r"myfile.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)