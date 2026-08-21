''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def numberOfTurns(self, root, p, q):
        def find_path(node, target, path):
            if not node:
                return False
            if node.data == target:
                return True
            if node.left:
                path.append('L')
                if find_path(node.left, target, path):
                    return True
                path.pop()
            if node.right:
                path.append('R')
                if find_path(node.right, target, path):
                    return True
                path.pop()
            return False
    
        path_p, path_q = [], []
        find_path(root, p, path_p)
        find_path(root, q, path_q)
    
        # Remove the common ancestor path to get paths from LCA
        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1
    
        s_p = path_p[i:]
        s_q = path_q[i:]
    
        def count_turns(path):
            return sum(1 for j in range(len(path) - 1) if path[j] != path[j + 1])
    
        # If LCA is p or q, only count turns on the single branch; otherwise include the turn at LCA (+1)
        if not s_p:
            turns = count_turns(s_q)
        elif not s_q:
            turns = count_turns(s_p)
        else:
            turns = 1 + count_turns(s_p) + count_turns(s_q)
    
        return turns if turns > 0 else -1 