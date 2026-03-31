class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}

        # target - currentNum = neededValue
        # look for neededValue in a hashmap of seen values

        for i, num in enumerate(nums): # Flipped i and num
            neededVal = target - num
            if neededVal in seenNums:
                return [seenNums[neededVal], i]
            else:
                seenNums[num] = i
                
        return []