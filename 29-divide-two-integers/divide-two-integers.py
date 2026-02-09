class Solution:
    def divide(self, dividend: int, divisor: int) -> int: 
            INT_MAX = 2147483647
            INT_MIN = -2147483648+1

            if(divisor < 0 and dividend > 0):
                divisor = -divisor
                P = dividend // divisor
                P = -P
                        
                if (P <= INT_MIN):
                    return INT_MIN
                else:
                    return P
                
            elif(dividend < 0 and divisor > 0):
                dividend = -dividend
                P = dividend // divisor
                P = -P
                        
                if (P <= INT_MIN):
                    return INT_MIN-1
                else:
                    return P
                
            else:
                P = dividend // divisor  
                
                if (P >= INT_MAX):
                    return INT_MAX
                else:
                    return P
      