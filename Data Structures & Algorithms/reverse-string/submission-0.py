class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1

        while i <= j:
            curr = ""
            if s[i] != s[j]:
                curr = s[i]
                s[i] = s[j]
                s[j] = curr
            i += 1
            j -= 1