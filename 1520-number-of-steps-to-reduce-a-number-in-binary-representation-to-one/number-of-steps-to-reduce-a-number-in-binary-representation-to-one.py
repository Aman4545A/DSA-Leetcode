# class Solution:
#     def numSteps(self, s: str) -> int:
#         a = int(s,2)
#         count = 0

#         while(a !=1):
#             if a%2==0:
#                 a= a//2
#                 count = count+1
#             else :
#                 a = a+1 
#                 count = count+1  

#         return count 

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry         
        