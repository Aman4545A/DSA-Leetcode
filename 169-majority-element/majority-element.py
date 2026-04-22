from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        count = 1
        max_count = 1
        result = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  

            if count > max_count:
                max_count = count
                result = nums[i]

        return result