'''A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.

Examples
is_disarium (75) → False # 7^1 + 5^2 = 7 + 25 = 32
is_disarium (135) → True # 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium (544) → False
is_disarium (518) -->True
is_disarium (466) → False
is_disarium (8) → True

Notes
• Position of the digit is 1-indexed.'''

#SOLUTION USING INITIALIZATION OF AN EMPTY LIST
a=input()
li=[]
for i in range(len(a)):
    b=int(a[i])**(i+1)
    li.append(b)
c=sum(li)
if c==int(a):
    print(True)
else:
    print(False)

#SOLUTION USING A DUMMY VARIABLE
a=input()
n=0
for i in range(len(a)):
    b=int(a[i])**(i+1)
    n=n+b
if n==int(a):
    print(True)
else:
    print(False)

a=input()
li=[int(a[i])**(i+1) for i in range(len(a))]
c=sum(li)
if c==int(a):
    print(True)
else:
    print(False)

#SOLUTION USING LIST COMPREHENSION
'''This method occupies less number of lines of code'''
a=input()
li=[int(a[i])**(i+1) for i in range(len(a))]
c=sum(li)
print(True) if c==int(a) else print(False)

#SOLUTION USING FUNCTION
def is_disarium(a):
    li=[int(a[i])**(i+1) for i in range(len(a))]
    c=sum(li)
    print(True) if c==int(a) else print(False)
a=input()
is_disarium(a)







