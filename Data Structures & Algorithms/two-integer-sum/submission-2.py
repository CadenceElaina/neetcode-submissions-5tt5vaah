class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}
        for i, num in enumerate(nums):
            neededValue = target - num
            if neededValue in seenNums:
                return[seenNums[neededValue], i]
            else:
                seenNums[num] = i
        
            