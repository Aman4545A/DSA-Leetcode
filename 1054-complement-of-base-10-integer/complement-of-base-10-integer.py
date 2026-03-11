class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = bin(n)
        s = num[2:len(num)]
        b = ""

        for i in s:
           if i=='0':
            b = b+'1'
           else:
             b = b+'0' 

        result = int(b, 2)
        return result   

              
        