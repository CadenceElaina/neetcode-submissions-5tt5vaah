class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - currentValue  = difference needed to sum to target
        #loop through list of nums
        # if the difference is in our hashmap we return that index + current index otherwise we add the current index:value to hashmap
        seenNums = {}
        for i, num in enumerate(nums):
                neededValue = target - num
                if neededValue in seenNums:
                    return[seenNums[neededValue], i]
                seenNums[num] = i