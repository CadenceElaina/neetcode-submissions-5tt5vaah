class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force - sort find lowest store count of longest continue until you reach a number increased by more than 1 -
        # update longest = max(longest, curr)
        #

        # store set of unique numbers seen
        # ask if curr number 
        # is curr +1 from prior?
        num_set=set(nums)

        longest_streak = 0
        for n in num_set:
            if(n - 1) not in num_set:
                current_num = n
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak
