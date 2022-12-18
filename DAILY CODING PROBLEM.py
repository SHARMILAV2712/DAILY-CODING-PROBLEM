'''This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''
##a=input().split()
##b=int(input())
##for i in a:
##    for j in a:
##        if (int(i)+int(j)) == b:
##            print(True)
##        break

##def present(a,b):
##    for i in a:
##        for j in a:
##            if (int(i)+int(j)) == b:
##                 return
##            break
##a=input().split()
##b=int(input())
##present(a,b)
##print(True)

##def present(x,y):
##    for i in x:
##        for j in x:
##            if (int(i)+int(j)) == y:
##                 return
##            break
##
##a=input().split()
##b=int(input())
##present(a,b)
##print(True)


'''This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''
##a= list(map(int,input().split(',')))
##b=[]
##n=1
##for i in range(len(a)):
##        n=n*a[i]
##ans=n
##for j in a:
##    tot=ans//j
##    b.append(tot)
##print(b)

##a= list(map(int,input().split(',')))
##b=[]
##n=1
##for i in range(len(a)):
##        n=n*a[i]
##for j in a:
##    tot=n//j
##    b.append(tot)
##print(b)

##def uber(a):
##    b=[]
##    n=1
##    for i in range(len(a)):
##        n=n*a[i]
##    for j in a:
##        tot=n//j
##        b.append(tot)
##    print(b)
##
##a=list(map(int,input().split(',')))
##uber(a)
















'''my code arose from the misunderstanding of the above. which gives the multiplication of all the elements with the element at the specified index except the element at the index'''
##a= list(map(int,input().split(',')))
##b=[]
##for i in range(len(a)):
##    n=i+1
##    while n<len(a):
##        ans=a[i]*a[n]
##        n = n+1
##        b.append(ans)
##print(sorted(b))

#without sorted, the ans will be 6 3 2 for the input
        
'''This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.'''

##a=list(map(int,input().split()))
##n=1
####for i in a:
####    if i<0:
####        a.remove(i)
##for j in range(1,len(a)+1):
##    if n not in a:
##        print(n)
##        break
##    elif j not in a:
##        print(j)
##        break
##else:
##    print(max(a)+1)

##a=list(map(int,input().split()))
##for j in range(1,len(a)+1):
##    if j not in a:
##        print(j)       #IF BREAK IS GIVEN STRAIGHT TO IF, NO OUTPUT AS IT BREAKS THE FOR LOOP
##        break                   #WITHOUT BREAK, IF ELSE IS GIVEN OUT SIDE THE IF, OUTPUT WILL BE PRINTED TWO TIMES
##else:
##    print(max(a)+1)

##def stripe(a):
##    for j in range(1,len(a)+1):
##        if j not in a:
##            print(j)                HOW TO DO THIS USING RETURN KEYWORD?
##            break                   IF WE GIVE ELSE STRAIGHT TO IF CONDITION IT WILL ITERATE LEN OF A NUMBER OF TIMES 
##    else:
##        print(max(a)+1)
##a=list(map(int,input().split()))
##stripe(a)


'''Writing short code
Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

What makes this tricky is that your function body must only contain a single line of code.'''

##def convert(a):
##    stri = map(str,a)
##    print (stri)
##a=list(map(int,input().split(",")))
##convert(a)

'''Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".'''

##def format_number(num):
##    n=-4
## 
##    for i in range(1,len(num)):
##        n=n*i
##        num1 = num[-1:-4]     WHY THIS RETURNS EMPTY SPACE?
##        print(num1)      
##num=input()
##format_number(num)
  
##num=input()
##n=-4
##n1=""
##for i in range(1,len(num)):
##        n=n*i
##        for j in a[-i]:
##            if -i==n
##        

##my_str =input()
##a=','.join(my_str[i:i+3] for i in range(0, len(my_str), 3))    final answer
##print(a)

a=list(input())
for i in range(1,len(a)):
    n=3*i
    a.insert((-n),',')
    print(a)
    


'''This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.'''

##anum=input()
####alp = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,
####       's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
##for i in a:
##    
##print(alp)

'''Write a function PentagonalNumber(num) read num which will be a positive integer and determine how many dots exist in a
pentagonal shape around a center dot on the Nth iteration. For example, in the image below you can see
that on the first iteration there is only a single dot, on the second iteration there are 6 dots, on the third there are 16 dots, and on the fourth there are 31 dots.
           o
 o      o o o
          o o
Your program should return the number of dots that exist in the whole pentagon on the Nth iteration.

Sample Test Cases

Input:2
Output:6

Input:5
Output:51'''

##a=int(input())
##n=1
##for i in range(a):
##    b=(5*i)
##    n=n+b
##print(n)
    














