class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [None] * 2*n

        for i in range(len(arr)):
            arr[i] = nums[(i%n)]

        return arr