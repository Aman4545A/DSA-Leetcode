class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        r = len(nums) - 1
        
        s = set()
        
        while i < r:
            avg = (nums[i] + nums[r]) / 2
            s.add(avg)
            i += 1
            r -= 1
        
        return len(s)
       
      
        