class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        left = 0
        right = len(nums) - 1
        #two cases: l and mid belong to the left sorted segment, or mid and r belong to the right sorted segment.
        #if l and mid are in the same segment, nums[l] < nums[mid], s
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # identify the sorted half
            if nums[left] <= nums[mid]:
                # left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid-1 # target is in sorted left half
                else:
                    left = mid+1 #target must be in right half
            else:
                # right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid +1 # target is in the sorted right half
                else:
                    right = mid -1 # target must be in left half
            
        return -1
        