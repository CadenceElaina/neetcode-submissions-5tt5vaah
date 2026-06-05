class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] + nums[j] = number needed
        freq = {}
        for i, n in enumerate(nums):
          need = target - n
          if need in freq:
            return [freq[need], i]
          freq[n] = i