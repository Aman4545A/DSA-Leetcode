class Solution:
    def reverseWords(self, s: str) -> str:
        a = ""

        words = s.split()

        for word in words:
            a += word[::-1] + " "

        return a.strip()
         

        