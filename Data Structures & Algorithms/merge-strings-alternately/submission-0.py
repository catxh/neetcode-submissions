from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = deque(word1)
        word2 = deque(word2)
        word3 = []

        while word1 and word2:
            word3.append(word1.popleft())
            word3.append(word2.popleft())
        
        if word1:
            word3.extend(word1)
        
        if word2:
            word3.extend(word2)
        
        return ''.join(word3)
        

