# 406. Queue Reconstruction by Height

## Date: 2019.12.1
[view in Leetcode](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Problem Description:
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
### Note:
    The number of people is less than 1,100.
### Example
    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    
    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

## Solution
我们先考虑如果先把个子高的排好序，那么在任何位置插入数据都不会对已经排好序的数组造成影响。而，与此同时，我们已经知道了个子高的排序，那么当新的数据到的时候，我们要确定它的位置也很简单，因为现在的所有数据都比他高，所以只要根据他的第二个数字确定他的位置即可。

```python

class Solution:
    def reconstructQueue(self, people):
        '''
        :param people: List[List[int]]
        :return: List[List[int]]
        '''
        result = []
        # 先用第一个关键字逆排序，然后在用第二关键字正向排序
        height_ascent = sorted(people, key=lambda x: (-x[0],x[1]))
        for height, pos in height_ascent:
            result.insert(pos, [height, pos])
        return result
        
```
