class Solution:
    def findMin(self, nums: List[int]) -> int:
        # one side is sorted the other is not
        # if its on sorted side perform bs
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]

