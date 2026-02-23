class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        i = 0
        while i < len(s):
            r = i
            while r < len(s):
                if s[i:r+1] == s[i:r+1][::-1]:
                    count += 1
                r += 1
            i += 1

        return count    
        