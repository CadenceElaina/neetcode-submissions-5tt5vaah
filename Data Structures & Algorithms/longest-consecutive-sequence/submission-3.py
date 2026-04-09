class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # track unique nums
        uniques = set(nums)
        longest = 0
        # if prev idx is not -1 from val we know its a new seq
        for num in uniques:
            if num-1 not in uniques:
                current = num
                current_streak = 1
                while current+1 in uniques:
                    current +=1
                    current_streak+=1
                longest = max(longest, current_streak)
        return longest
