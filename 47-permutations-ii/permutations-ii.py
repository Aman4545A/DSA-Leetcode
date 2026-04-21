class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set(itertools.permutations(nums, len(nums)))
        return [list(x) for x in perms]
        