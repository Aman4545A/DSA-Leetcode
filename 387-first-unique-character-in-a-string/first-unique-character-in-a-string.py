class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = ""

        for ch in s:
            if s.count(ch) == 1:
                result += ch

        if result == "":
            return -1  

        return s.index(result[0])


            
        