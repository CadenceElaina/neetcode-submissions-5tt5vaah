class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
#a + b + c
# a, L, R
        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            l = i +1
            r = len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    # theyre equal to 0 !
                    res.append([a, nums[l], nums[r]])
                    l += 1 # advance left pointer until we reach a new value
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

       
        
