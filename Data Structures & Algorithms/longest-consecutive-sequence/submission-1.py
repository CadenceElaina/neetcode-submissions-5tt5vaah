class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        largestSequence = 0
        
        for num in uniqueNums:
            # if the num - 1 doesnt exist we know its a start of a new sequence
            if (num-1) not in uniqueNums:
                currentNum = num
                currentStreak = 1

                while (currentNum + 1) in uniqueNums:
                    currentNum +=1 # move pointer forward
                    currentStreak +=1 
                
                largestSequence = max(largestSequence, currentStreak)
        
        return largestSequence