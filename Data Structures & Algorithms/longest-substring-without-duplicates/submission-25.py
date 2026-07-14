class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = []
        length = 0

        for char in s:
            if char not in window:
                window.append(char)
            else:
                length = max(length, len(window))

                while window and window[0] != char:
                    window.pop(0)

                window.pop(0)
                window.append(char) 

        return max(length, len(window))