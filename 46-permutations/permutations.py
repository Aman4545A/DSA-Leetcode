class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = list(itertools.permutations(nums, len(nums)))
        return perms
        