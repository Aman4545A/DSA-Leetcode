class Solution:
    def moveZeroes(self, nums: List[int]) -> None:      
                n = len(nums)
                pos=0
                for i in range(n):
                    if(nums[i]!=0):
                        nums[pos]=nums[i]
                        pos = pos+1

                while pos < n:
                    nums[pos]=0
                    pos=pos+1
                 
        