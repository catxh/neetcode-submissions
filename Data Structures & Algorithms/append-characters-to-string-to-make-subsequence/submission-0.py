class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        tub = 0
        for sub in s:
            if tub == len(t):
                break
            if t[tub] == sub:
                tub += 1
        return len(t) - tub
        