'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''
        
class Solution:
    def absDiff(self, root):
        prev = None
        min_diff = float("inf")

        def inorder(node):
            nonlocal prev, min_diff
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                min_diff = min(min_diff, node.data - prev)
            prev = node.data
            inorder(node.right)

        inorder(root)
        return min_diff