class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        f = s = t = float('-inf')   
        min1 = min2 = float('inf') 

        for x in nums:
            if x > f:
                t = s
                s = f
                f = x
            elif x > s:
                t = s
                s = x
            elif x > t:
                t = x

    
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return max(f * s * t, f * min1 * min2)

        