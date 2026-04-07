class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        freq = {}

        for i, c in enumerate(s):
            if c in freq:
                l = max(l, freq[c]+1)
            freq[c] = i
            longest = max(longest, i - l +1 ) # + 1?
            #longest = max(longest, i - freq.get(c) ) 


        return longest
        
            
            