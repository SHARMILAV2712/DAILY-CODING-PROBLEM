'''This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''

#SOLUTION
a= list(map(int,input().split(',')))
b=[]
n=1
for i in range(len(a)):
        n=n*a[i]
for j in a:
    tot=n//j
    b.append(tot)
print(b)

#SOLUTION USING FUNCTION
def uber(a):
    b=[]
    n=1
    for i in range(len(a)):
        n=n*a[i]
    for j in a:
        tot=n//j
        b.append(tot)
    print(b)

a=list(map(int,input().split(',')))
uber(a)

#ALGORITHM
'''By seeeing the question, we could think that it may take many lines to complete the code.
but, once we found the algorithm, it is so simple to write the code.
The algorithm goes here...
To get the product of all the numbers except the number at the particular index,
>>first multiply all the numbers in the index and store it in a variable.
>>then using loop method, divide the stored number by the number at the specified index during every iteration
>>return the results as a list.'''
        
