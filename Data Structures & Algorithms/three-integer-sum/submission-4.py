class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #  loop through outer
        # then loop using 2 pointers inner

        for i, num in enumerate(nums):
            # if we are not at the first index and the previous value in nums is equal to current num
            # continue advancing i until we find a new number 
            if i > 0 and nums[i - 1] == num:
                continue
            l = i+1
            r = len(nums)-1
            while(l < r):
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum < 0:
                    l +=1
                else:
                    res.append([num, nums[l], nums[r]])
                    # must advance pters to prevent infinite loop
                    l += 1 # advance left pointer until we reach a new value 
                    # while current value at left pointer == nums[l-1] prev val and l<r continue advancing l
                    # sorted but may contain repeat vals
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
