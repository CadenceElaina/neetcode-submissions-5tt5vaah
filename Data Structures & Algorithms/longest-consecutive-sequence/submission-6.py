class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest_streak = 0

        for n in n_set:
            if (n-1) not in n_set:
                current_n = n
                current_streak = 1

                while(current_n + 1) in n_set:
                    current_streak += 1
                    current_n += 1
                
                longest_streak = max(longest_streak, current_streak)
        return longest_streak