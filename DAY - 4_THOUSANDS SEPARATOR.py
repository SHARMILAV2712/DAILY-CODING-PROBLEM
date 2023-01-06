''' DAY - 4
Write a function named format_number that takes a non-negative number as its only parameter.
Your function should convert the number to a string and add commas as a thousands separator.
For example, calling format_number(1000000) should return "1,000,000".'''

#SOLUTION
#We used python string format syntax
def format_number(a):
    print(f"{a:,}")
a=int(input())
format_number(a)
