# 739. Daily Temperatures
[view in Leetcode](https://leetcode.com/problems/daily-temperatures/)
## Date: 2019-12-1
## Problem Description:
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures ```T = [73, 74, 75, 71, 69, 72, 76, 73]```, your output should be ```[1, 1, 4, 2, 1, 1, 0, 0]```.

### Note: 
    The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## Solution: 
### Solution 1: This solution may time out
```python
class Solution:
    def dailyTemperatures(self, T):
        '''
        :param T: List[int]
        :return: List[int]
        '''
        result = []
        for i in range(len(T)):
            max_value = (T[i], i)
            index = 0
            for j in range(i+1, len(T)):
                if T[j] > max_value[0]:
                    index = j - max_value[1]
                    break
            result.append(index)
        return result
```
### Solution2: 
The general idea of the "stack" approach is that you run through the array forward and push onto the stack the index of each element (i.e.: 1, 2, 3, etc; in order). At each step, before pushing, you see if the value that the stack top index references is less than the current; if that's the case you pop the index off the stack and record the answer; repeat with the new top of stack.

Note that although there's a nesting of loops, the inner loop iterates at most len(temperatures) times in total for the whole program, not len(temperatures) times for each outer loop — a total number. Therefore the runtime is O(n).
```python
class Solution:
    def dailyTemperatures(self, T):
        '''
        :param T: List[int]
        :return: List[int]
        '''
        stack = []
        wait = [0]*len(T)
        for i in range(len(T)):
            while len(stack) > 0 and T[stack[-1]] < T[i]:
                j = stack.pop()
                wait[j] = i-j
            stack.append(i)
        return wait
```
