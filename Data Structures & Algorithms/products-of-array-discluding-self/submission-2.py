class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # so we loop through the array left to right and store all values to the left of our index and we dont need to worry about checking a bad index in python ig? starting at 0 still works instead of 1 and we set the index in the prefix array at that index to be our running prefix which at index 0 would just be 1 by default --- then we update running_prefix to be equal to 1 * our current value so that the next index will properly get 1 * prev index val --- whereas the 2nd iteration is doing the opposite - loop right to left and gather the values to the right of the current index so at the last index we start with running_suffix of 1 (no values to the right of last index) but we update running_suffix *= value at current index then at len(nums)-1 we do the same thing right its value of 4 in our example and we push that to our curr index of the suffixArr and we update running_suffix to be 1*4*3 right then we pass a 3rd time to do the calculations which is prefixArr[i] * suffixArr[i] which gives us the multiplication of all values to the left and right of that index such that the result array has the correct calculations exlcuding the val at index i 
        # O(n) w/o division operation
        # return array of products of each index except that index

        # loop through array then loop through at each index to find values of other indexes multiplied together
        # o(n^2)? bad solution

        # instead we should probably store previous calculations in an array
        # prefix + suffix technique to avoid duplicate work
        # iterate left to right and store the prefix products for each index in a prefix array, excluding the currnet index's number
        # Then we iterate from right to left and store the suffix products for each index in a suffix array, also excluding current index's number
        n = len(nums)
        output = [1] * n #
        prefixArr = [1] * n #stores the products of all numbers left of index i
        suffixArr = [1] * n #stores the products of all numbers to the right of index i
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
