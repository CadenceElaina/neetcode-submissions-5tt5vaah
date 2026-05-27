class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_s = nums[0]
        curr_s = 0
        for n in nums:
            if curr_s < 0:
                curr_s = 0
            curr_s += n
            max_s = max(max_s, curr_s)
          #
            #if max_s + nums[n] < 0:
           #     max_s = 0
            #max_s += nums[n] 

        return max_s