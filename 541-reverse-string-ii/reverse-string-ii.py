class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        first = ""
        i = 0

        while i < len(s):
            p = s[i:i+k]
            q = s[i+k:i+2*k]

            first = first + p[::-1] + q
            i = i + 2 * k

        return first  


        