class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The sorted half is either the first or second half.
        # We identify it by comparing the first index against the mid index.
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m

            # Identify the sorted half
            if nums[l] <= nums[m]:
                # Left half is sorted
                # Is our target within this sorted range?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    # Target must be in the right half
                    l = m + 1
            else:
                # Right half is sorted
                # Is our target within this sorted range?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    # Target must be in the left half
                    r = m - 1

        return -1