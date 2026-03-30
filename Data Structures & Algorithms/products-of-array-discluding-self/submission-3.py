class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefixArr = [1] * n #stores the products of all numbers left of index i
        suffixArr = [1] * n #stores the products of all numbers right of index i
        running_prefix =1 
        running_suffix = 1

        for i in range(n):
            prefixArr[i] = running_prefix
            running_prefix *= nums[i]
        
        for i in range(n - 1, -1, -1):
            suffixArr[i] = running_suffix
            running_suffix *= nums[i]
        
        for i in range(n):
            output[i] = prefixArr[i] * suffixArr[i]

        return output