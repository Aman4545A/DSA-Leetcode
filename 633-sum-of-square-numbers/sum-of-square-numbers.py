class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(c ** 0.5)

        while i <= j:
            s = i * i + j * j

            if s == c:
                return True
            elif s > c:
                j -= 1
            else:
                i += 1

        return False


        