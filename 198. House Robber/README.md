# 198. House Robber
[view in leetcode](https://leetcode.com/problems/house-robber/)

## Problem  Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

### Example 1:

    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.
### Example 2:

    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                 Total amount you can rob = 2 + 9 + 1 = 12.

## Solution:
### Solution1: recursion and memorization
```python
class  Solution:
    # recursion and memoization
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        total_amount = [-1]*n

        def rob_(nums, i):
            if i < 0:
                return 0
            if total_amount[i] >= 0:
                return total_amount[i]
            total_amount[i] = max(rob_(nums, i-2) + nums[i], rob_(nums, i-1))
            return total_amount[i]

        return rob_(nums, n-1)
```

### solution2 : Dp
```python
class Solution:
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        else:
            dp = [0] * n
            for i in range(n):
                # dp是已经经过了i个房子，之前的房子可以抢也可以不抢. dp 用来记录之前经过房子的最大值
                dp[i] =max((dp[i-2]+nums[i] if i > 1 else nums[i]), (dp[i-1] if i > 0 else 0))
        return dp[-1]
```
