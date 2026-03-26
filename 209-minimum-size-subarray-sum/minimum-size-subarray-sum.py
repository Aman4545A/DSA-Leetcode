class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        sum = 0 
        min_len = float('inf')  

        for j in range(len(nums)):
            sum = sum+nums[j] 

            while(sum >= target):
              min_len = min(min_len, j-i+1)
              sum = sum-nums[i]  
              i = i+1  

        return 0 if min_len == float('inf') else min_len             
                    


        