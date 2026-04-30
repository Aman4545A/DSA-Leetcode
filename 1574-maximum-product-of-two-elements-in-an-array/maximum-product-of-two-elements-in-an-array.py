class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        F = S = 0

        for num in nums:
            if num > F:
                S = F
                F = num
            elif num > S:
                S = num

        return (F - 1) * (S - 1)