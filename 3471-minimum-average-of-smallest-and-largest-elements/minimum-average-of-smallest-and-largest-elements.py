class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0 
        right = len(nums) - 1
        minv = float('inf')

        while left < right:
            avg = (nums[left] + nums[right]) / 2
            minv = min(minv, avg)
            left += 1
            right -= 1

        return minv



        