class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # loop through string
        # find most occurances of same character
        # Consider: aaaabbaabbbbbb k=2. Loop through count different letters - ran out of "lives / k" k=0 or other var for k
        # continue until we reach index different than "a" which is idx 8 so then we look at where we used our Ks
        # and look at the character at idx 8 is the gap between viable to use k on? to make the characters at 8 on extend to where 
        # we used our Ks in prior substring? if so we set start to idx 4 in this example and swap 6 and 7 and continue
        # until end of str and update our max substring len at that point

        #Instead of tracking the swaps, just track the frequencies of the characters currently inside your window.
        #  To know if your current window is valid (meaning you can make all letters the same using <= k swaps)
        # we track 3 things:
        # 1. The size of our window.
        # 2. The count of the most frequent character in that window.
        # 3. Our allowed swaps (k).
        # valid window: (Window Length) - (Count of Most Frequent Character) <= k
        # if it exceeds k then we need to shrink it from the left
        # [a, b, c, a] k = 1
        # length is 4 most freq is 'a' count (2)
        # 4 - 2 = 2
        # 2 > 1, so this window is invalid.
        # to fix we move left forward by one space. 

        l = 0
        maxLen = 0
        charMap = {}
        for i, c in enumerate(s):
            charMap[c] = charMap.get(c, 0)+1
            mostSeenChar = max(charMap.values())
            #Check validity of window
            windowSize = (i - l +1)
            if (windowSize - mostSeenChar) > k:
                charMap[s[l]] -= 1
                l += 1
            #enforce shrink
        #    windowSize = (i-l+1)
         #   charMap[c[l]] = charMap.get(c,2)-1
            maxLen = max(maxLen, i - l + 1)
        return maxLen
                    
#            if c in charMap:
             #   charMap[c] = charMap.get(c, 0)+1 # need to practice this syntax

