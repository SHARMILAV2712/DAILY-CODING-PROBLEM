'''This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].'''

#SOLUTION:
a=list(input().split(','))
b=input()
li=[]
for i in a:
    c=i[:len(b)]
    if c==b:
        li.append(i)
print(li)

#SHRINKEN SOLUTION:
def twitter(wordlist, prefix):
    return [word for word in wordlist if word[:len(prefix)] == prefix ]
wordlist=list(input().split(','))
prefix=input()
twitter(wordlist,prefix)

#DESCRIPTION
'''In the above code we used list comprehension.
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
SYNTAX:
        newlist = [expression for item in iterable if condition == True]'''

#SOLUTION USING FUNCTION
def twitter(a,b):
    li=[]
    for i in a:
        c=i[:len(b)]
        if c==b:
            li.append(i)
    print(li)
a=list(input().split(','))
b=input()
twitter(a,b)
