class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in hm:
                return [hm[needed], i]
            hm[n] = i
        