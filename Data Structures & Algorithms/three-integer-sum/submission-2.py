class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
#a + b + c
# a, L, R
        for i, a in enumerate(nums):
            # check if not index 1 and if prev value == curr val - if so advance bc we cant have dups
            if i > 0 and nums[i-1] == a:
                continue # dont reuse same val
            l = i + 1
            r = len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else: # equals to zero
                    res.append([a, nums[l], nums[r]])
                    #     L                    R
                    # [-2, -2, 0, 0, 2, 2]
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l  += 1


        return res

       
        
