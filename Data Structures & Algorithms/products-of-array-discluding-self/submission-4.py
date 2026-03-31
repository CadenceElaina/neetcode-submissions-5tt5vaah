class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n
        prefixArr = [1] * n # stores product of numbers left of index i
        suffixArr = [1] * n # stores product of numbers right of index i
        runningPrefix = 1
        runningSuffix = 1
        # loop once to get prefix
        for i in range(n):
            prefixArr[i] = runningPrefix
            runningPrefix *= nums[i]
        # loop to get suffix
        for i in range(n - 1, -1, -1):
            suffixArr[i] = runningSuffix
            runningSuffix *= nums[i]
        # loop to multiple prefix and suffix
        for i in range(n):
            output[i] = prefixArr[i] * suffixArr[i]

        return output