class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix=1
        suffix=1
        res=[1]*n

        #loop through get prefix
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        #loop through get suffix vals
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix*=nums[i]
        return res
