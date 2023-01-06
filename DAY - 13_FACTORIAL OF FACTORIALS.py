'''DAY 13
FACTORIAL OF FACTORIALS
Create a function that takes an integer n and returns the factorial of factorials.
See below examples for a better understanding:

Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200'''

#GENERAL SOLUTION
a=int(input())
n=1
for i in range(1,a+1):         
    for j in range(1,i):
        n=n*j
    n=n*i
print(n)

#SOLUTION USING FUNCTION
def fact(a):
    n=1
    for i in range(1,a+1):         
        for j in range(1,i):
            n=n*j
        n=n*i
    print(n)
a=int(input())
fact(a)

#SOLUTION USING INBUILT MATH MODULE
'''This reduces the loop count'''

import math
a=int(input())
n=1
for i in range(a+1):
    n=math.factorial(i)*n
print(n)







