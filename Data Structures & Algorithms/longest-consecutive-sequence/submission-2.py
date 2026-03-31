class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        largestSeq = 0

        for num in uniqueNums:
            if (num-1) not in uniqueNums:
                # s tart of a new seq.
                currentNum = num
                currentStreak = 1
                while (currentNum + 1) in uniqueNums:
                    currentNum +=1
                    currentStreak +=1
                
                largestSeq = max(largestSeq, currentStreak)
        return largestSeq

        # need to check for: if at num 5 if there is a 4 behind it - if not its a new sequence