class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in hm:
                return [hm[need], i]
            hm[n] = i