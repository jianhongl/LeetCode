# 647. Palindromic Substrings
[view in Leetcode](https://leetcode.com/problems/palindromic-substrings/)

## Problem Description
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

### Example 1:

    Input: "abc"
    Output: 3
    Explanation: Three palindromic strings: "a", "b", "c".
 

### Example 2:

    Input: "aaa"
    Output: 6
    Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

### Note:

    The input string length won't exceed 1000
    
## Solution
### Solution 1: DP
```python
class Solution:
    # dp 对于一个 j 到 i（j<i) 的字符串，它是回文串，当且仅当 i 与 j 处值相等并且 j+1 到 i-1 的子串也满足条件
    # dp[i, j] = 1                                   if i == j
    #          = s[i] == s[j]                        if j = i + 1
    #          = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1
    def countSubstrings(self,s):
        '''
        :param s: str
        :return: int
        '''
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if i - j < 2:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = ((s[i] == s[j]) and (dp[j+1][i-1]))
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count
```
