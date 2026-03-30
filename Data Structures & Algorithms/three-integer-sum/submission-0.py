class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return nested list if more than one correct result
        # no matches return empty array
        # nums[i] + nums[j] + nums[k] == 0 
        # i mean loop through array and check if the current value  with two others = 0
        # so on that value we run a two pointer approach with left and right indexes
        # to check all numbers except our current to see if the current smallest value / pointer + our largest pointer from the other side + our current number in outter loop == 0 if so add it to list as a list. 


        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum <0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
        return res
                    # [-2, -2, 0, 0, 2, 2]

       
        
