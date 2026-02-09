class Solution(object):
    def myAtoi(self,s):
        s = s.lstrip()
        
        if not s:
            return 0

        sign = 1
        i = 0
        result = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        result = result * sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result
        
        