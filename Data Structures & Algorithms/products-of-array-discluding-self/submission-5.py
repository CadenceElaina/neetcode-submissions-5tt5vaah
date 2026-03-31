class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefixArr = [1] * n
        suffixArr = [1] * n
        running_prefix = 1
        running_suffix = 1

        # products of suffix
        for i in range(n):
            prefixArr[i] = running_prefix
            running_prefix *= nums[i]
        # producs of prefix
        for i in range(n-1, -1, -1): # for i in range(start, stop, start)
            suffixArr[i] = running_suffix
            running_suffix *= nums[i]

        # for each index prodcutsofarrayexceptself= prefix[i] * suffix[i]
        for i in range(n):
            output[i] = prefixArr[i] * suffixArr[i]
        
        return output