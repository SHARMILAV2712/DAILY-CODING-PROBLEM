'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

#SOLUTION
a=list(map(int,input().split(',')))
b=int(input())
for i in a:
    for j in a:
        if (i+j) == b:
            print(True)
        break

#SOLUTION USING FUNCTION
def present(a,b):
    for i in a:
        for j in a:
            if (i+j) == b:
                 return
            break
a=list(map(int,input().split(',')))
b=int(input())
present(a,b)
print(True)

#SOME SHORT DESCRIPTIONS:
    '''In-built functions used in this code are:
        * map - It is used for transforming all the items in an iterable without using an explicit for  loop.
                    The code takes less number of lines and takes less time to run.
        * split - This function splits the string based on our specification (whitespace as default) into list.
        * Difference between print and return inside def function:
            --> print displays the value to the user.
            --> prints value for all possible occurance.
            --> return is a keyword where program stop its execution of the current function.
            --> Returns the value for the first occurance.'''
        
