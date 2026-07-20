class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        let_s = 0
        if not s:
            return True
        if s and t:
            for letter in range(len(t)):
                if t[letter] == s[let_s]:
                    let_s += 1
                if let_s == len(s):
                    return True
            if let_s == len(s):
                return True
        return False
