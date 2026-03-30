class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) w/o division operation
        # return array of products of each index except that index

        # loop through array then loop through at each index to find values of other indexes multiplied together
        # o(n^2)? bad solution

        # instead we should probably store previous calculations in an array
        # prefix + suffix technique to avoid duplicate work
        # iterate left to right and store the prefix products for each index in a prefix array, excluding the currnet index's number
        # Then we iterate from right to left and store the suffix products for each index in a suffix array, also excluding current index's number
        n = len(nums)
        output = [1] * n
        prefixArr = [1] * n
        suffixArr = [1] * n
        running_prefix = 1
        running_suffix = 1

        for i in range(n):
            # store current running_prefix into prefixArr[i]
            prefixArr[i] = running_prefix
            # update the running_prefix by multiplying it by nums[i]
            running_prefix *= nums[i]
        # PASS 2: Right to left

        for i in range(n -1, -1, -1):
            suffixArr [i] = running_suffix
            running_suffix *= nums[i] 
        # same concept but backwards

        # PASS 3: Multiply them together
        for i in range(n):
            output[i]= prefixArr[i] * suffixArr[i]

        return output
