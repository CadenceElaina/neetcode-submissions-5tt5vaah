class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        left = 0
        freq = {}
        longest = 0

        for right in range(len(s)):
            #update count for char
            freq[s[right]] = 1 + freq.get(s[right], 0)
        # update max seen char in our window
            longest = max(longest, freq[s[right]])
            # if window length - current longest seen char in this window > k - move left until we reach valid window
            # window length = (right - left) + 1 
            while (right - left + 1) - longest > k:
                freq[s[left]] -= 1
                left += 1
            
            # update max seen
            res = max( res, right-left+1)
        return res
