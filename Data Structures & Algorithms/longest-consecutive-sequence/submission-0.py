class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # return longest consecutive sequence of elems possible
        # any starting point but it must increase by 1 each time 
        # O(n)
        # brute force would be O(n^2) at least and you would essentially loop through array and check index against all other indexes and keep track of highest count possible or something idk
        # optimal sol O(n) - loop through once and track if current index is +1 or -1 from our seen values 
        # keep track of each sequence using a freqmap or dictionary within a list each key is the length and the value is all values in that sequence

        # use a set for O(1) lookups - does the number x-1 or x+1 exist? 
        # only need to know if the numbers exist and what the max length you've found so far
        # if n-1 is not in the set then we know the number is the start of a sequence

        uniqueNums = set(nums)
        largestSequence = 0

        for num in uniqueNums:
            # if the num - 1 doesnt exist we know its a start of a new sequence
            if(num-1) not in uniqueNums:
                currentNum = num
                currentStreak = 1

                while (currentNum + 1) in uniqueNums:
                    currentNum +=1 #move pointer forward
                    currentStreak+=1
                    
                largestSequence = max(largestSequence, currentStreak)

        return largestSequence