class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {} # takes number as key and stores the index as value - stores neededNumbers potentially 

#forgot the in keyword for enumerate as well
        for i, num in enumerate(nums):
            neededValue = target - num
            if neededValue in seenNums:
                return [seenNums[neededValue], i]
            else:
                seenNums[num] = i
                # take number and set it as key in our dictionary : value = i
                # if key exists update value to be +1 otherwise set it to be 1
                # had to get gemini to tell me syntax for this:
                # seenNums[num] = seenNums.get(num, 0) + 1
        return False