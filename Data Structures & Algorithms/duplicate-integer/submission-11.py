class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()

        for num in nums:
            if num in uniqueNums:
                return True
            uniqueNums.add(num)
        return False
