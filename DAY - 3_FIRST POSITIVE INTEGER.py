'''This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.'''

#SOLUTION 1
a=list(map(int,input().split()))
n=1
for j in range(1,len(a)+1):
    if n not in a:
        print(n)
        break
    elif j not in a:
        print(j)
        break
else:
    print(max(a)+1)

#SOLUTION 2
a=list(map(int,input().split()))
for j in range(1,len(a)+1):
    if j not in a:
        print(j)       
        break
    else:
    print(max(a)+1)

#SOLUTION USING FUNCTION
def stripe(a):
    for j in range(1,len(a)+1):
        if j not in a:
            print(j)                
            break                   
    else:
        print(max(a)+1)
a=list(map(int,input().split()))
stripe(a)








