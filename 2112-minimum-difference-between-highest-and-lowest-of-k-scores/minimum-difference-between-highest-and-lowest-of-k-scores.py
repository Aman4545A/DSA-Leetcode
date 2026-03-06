class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n= len(nums)
        s = float('inf')

        for i in range(n-k+1):
            diff = nums[i+k-1]- nums[i] 
            s = min(s, diff)

        return s    
            


        