# 763. Partition Labels

[view in Leetcode](https://leetcode.com/problems/partition-labels/)

## Problem Description
A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

###  Example 1:
    Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

###  Note:
    S will have length in range [1, 500].
    S will consist of lowercase letters ('a' to 'z') only.

## Solution
```python
class Solution:
    def partitionLabels(self, S):
        last_index = {}
        for i, ch in enumerate(S):
            last_index[ch] = i
        start = end = 0
        ans = []
        for i, ch in enumerate(S):
            end = max(end, last_index[ch])
            if i == end:
                ans.append(end - start + 1)
                start = end  + 1
        return ans
```
记录下每个元素的最后的位置
