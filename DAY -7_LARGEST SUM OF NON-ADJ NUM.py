'''DAY - 7
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13,
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.'''

#SOLUTION
def findMaxSum(a, n):
    dp = [[0 for i in range(2)] for j in range(n)]
    if (n == 1):
        return a[0]
    dp[0][0] = 0
    dp[0][1] = a[0]
    for i in range(1,n):
        dp[i][1] = dp[i - 1][0] + a[i]
        dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])
    return max(dp[n - 1][0], dp[n - 1][1])
a = list(map(int,input().split(',')))
n = len(a)
print(findMaxSum(a, n))
