class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, n in enumerate(nums):
            needed_num = target - n
            if needed_num in freq:
                return [freq.get(needed_num), i]
            freq[n] = i