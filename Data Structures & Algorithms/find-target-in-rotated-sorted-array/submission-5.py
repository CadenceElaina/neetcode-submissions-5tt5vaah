class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m 
            if nums[l] <= nums[m]: # then its sorted side
                if target > nums[m] or target < nums[l]: # is our target in other half?
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1