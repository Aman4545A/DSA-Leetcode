class Solution:
    def addBinary(self, a: str, b: str) -> str:

        s = int(a,2)
        a = int(b,2)

        c = s+a
        return (bin(c)[2:])
         