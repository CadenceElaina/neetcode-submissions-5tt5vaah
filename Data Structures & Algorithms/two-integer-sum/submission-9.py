class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # neededVal = target - nums[i]
        # see if neededval is in our hm - return true if so
        hm = {}
        for i, n in enumerate(nums):
            needed = target - n
            if needed in hm:
                return [hm[needed], i]
            hm[n] = i
        