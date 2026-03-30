class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # look at middle value is it greater than or less than our target
        # if mid val is too low then are new bounds are just 0 - mid-1 && new mid = top bound + bottom bound / 2
        # do opposite if too high
        l = 0
        r = len(nums) -1
        while(l <= r):
            mid = (r + l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return -1