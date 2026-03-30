class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            uniques = set()
            uniques = set()
            for num in nums:
                if num in uniques:
                    return True
                else:
                    uniques.add(num)
            
            return False
