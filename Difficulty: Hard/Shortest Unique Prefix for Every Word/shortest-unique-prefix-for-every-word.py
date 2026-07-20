class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

class Solution:
    def findPrefixes(self, arr):
        root = TrieNode()
        
      
        for word in arr:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                curr.freq += 1

        res = []
        
      
        for word in arr:
            prefix = []
            curr = root
            for char in word:
                prefix.append(char)
                curr = curr.children[char]
                if curr.freq == 1:
                    break
            res.append("".join(prefix))
            
        return res