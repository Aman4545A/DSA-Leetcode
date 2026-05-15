class Solution:
    def numTrees(self, n: int) -> int:
        fact1 = math.factorial(n)
        fact2 = math.factorial(2 * n)
        fact3 = math.factorial(n + 1)

        return fact2 // (fact1 * fact3)