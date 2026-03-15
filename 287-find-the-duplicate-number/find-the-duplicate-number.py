class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)
        for num in nums:
            if num in s:
                return num
            s.add(num)    
           

        return s        
        