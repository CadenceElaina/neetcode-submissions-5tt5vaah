class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (r + l) // 2
            if nums[m] > nums[r]:
                l = m + 1 # min is to the right
            else:
                r = m # if its not larger it could be the min val so keep it within bounds [l - r]
        return nums[l]