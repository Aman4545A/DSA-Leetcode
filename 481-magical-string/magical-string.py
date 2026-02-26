class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2         
        next_num = 1  

        while len(s) < n:
            count = s[i]
            s.extend([next_num] * count)
            next_num = 2 if next_num == 1 else 1
            i += 1

        return s[:n].count(1)