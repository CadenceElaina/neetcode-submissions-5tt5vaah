class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =  len(nums)
        output = [1] * n
        suffix = [1] * n
        running_suffix = 1
        prefix = [1] * n
        running_prefix = 1
        #products of suffix (RIGHT TO LEFT)
        for i in range(n - 1, -1, -1):
            suffix[i]= running_suffix
            running_suffix *= nums[i]
        #products of prefix
        for i in range(n):
            prefix[i] = running_prefix
            running_prefix *= nums[i]
        
        # calculate prodcuts 
        for i in range(n):
            output[i] = prefix[i] * suffix[i]
            
        return output