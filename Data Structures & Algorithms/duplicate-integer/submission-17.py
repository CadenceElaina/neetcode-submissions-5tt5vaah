class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm= {}

        for i in nums:
            if i in hm:
                return True
            hm[i] = hm.get(i, 0) +1
        return False
