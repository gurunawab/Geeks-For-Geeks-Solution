"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""


from collections import deque


class Solution:

  def areAnagrams(self, root1, root2):
    q1, q2 = deque([root1]), deque([root2])

    while q1 and q2:
      if sorted(node.data for node in q1) != sorted(node.data for node in q2):
        return False
      q1 = deque(c for node in q1 for c in (node.left, node.right) if c)
      q2 = deque(c for node in q2 for c in (node.left, node.right) if c)

    return not q1 and not q2 