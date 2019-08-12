# 965. Univalued Binary Tree

[view in Leetcode](https://leetcode.com/problems/univalued-binary-tree/)

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

### Example 1:
        1
       / \
      1   1
     / \   \
    1   1   1
    
    Input: [1,1,1,1,1,null,1]
    Output: true


### Example 2:
        2
       / \
      2   2
     / \
    5   2
    
    Input: [2,2,2,5,2]
    Output: false