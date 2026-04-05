class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # two cases: l and mid belong to the left sorted segment, or mid and r belong to the right sorted segment.

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Identify the sorted half
            if nums[left] <= nums[mid]:
                # is our target between the mid and left pointers?
                if nums[left] <= target < nums[mid]: 
                    right = mid - 1 # target is in our sorted left half
                else:
                    left = mid + 1 # target is in right half
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 # target is in the sorted right half
                else:
                    right = mid -1 #target is in our left half
        return -1
        