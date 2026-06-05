class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if not len(s) == len(nums):
          return True
        return False