''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        res = float('-inf')
    
        def dfs(node):
            nonlocal res
            if not node: 
                return float('inf')
            if not node.left and not node.right: 
                return node.data
    
            min_child = min(dfs(node.left), dfs(node.right))
            res = max(res, node.data - min_child)
            return min(node.data, min_child)
    
        dfs(root)
        return res 