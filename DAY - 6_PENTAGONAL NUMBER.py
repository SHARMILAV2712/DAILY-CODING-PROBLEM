'''DAY - 6
Write a function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a
pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see
that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots.
           o
 o      o  o  o
         o   o
Your program should return the number of dots that exist in the whole pentagon on the Nth iteration.

Sample Test Cases

Input:2
Output:6

Input:5
Output:51'''

#SOLUTION 1
a=int(input())
n=1
for i in range(a):
    b=(5*i)
    n=n+b
print(n)

#SOLUTION WITH FUNCTION
def pentagonalNumber(num):
    ans = 1
    for i in range(num):
        a=5*i
        ans = ans+a
    print(ans)
num = int(input())
pentagonalNumber(num)





        
        
