''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        self.preIndex = 0
        
        def solve(preMirrorStart, preMirrorEnd):
            if self.preIndex >= len(pre) or preMirrorStart > preMirrorEnd:
                return None
            
           
            root = Node(pre[self.preIndex])
            self.preIndex += 1
            
           
            if preMirrorStart == preMirrorEnd:
                return root
            
           
            i = preMirrorStart
            while i <= preMirrorEnd:
                if preMirror[i] == pre[self.preIndex]:
                    break
                i += 1
            
            if i <= preMirrorEnd:
                
                root.left = solve(i, preMirrorEnd)
                root.right = solve(preMirrorStart + 1, i - 1)
                
            return root

        return solve(0, len(pre) - 1)