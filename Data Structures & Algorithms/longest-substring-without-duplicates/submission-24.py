
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        length = 0
        for char in s:
            if char not in window:
                window.append(char)
            elif char in window:
                length = max(length, len(window))
                while window and window[0] != char:
                    window.pop()
                    continue
        return max(length, len(window))