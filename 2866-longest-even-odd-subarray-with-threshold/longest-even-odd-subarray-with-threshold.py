class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        curr = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                curr = 0
            elif curr == 0:
                if nums[i] % 2 == 0:
                    curr = 1
            elif nums[i] % 2 != nums[i-1] % 2:
                curr += 1
            else:
                curr = 1 if nums[i] % 2 == 0 else 0

            ans = max(ans, curr)

        return ans