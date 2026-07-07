class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # Window Length - Most Freq Char = Number of Swaps needed to make window valid
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1
            # we now have a valid window
            res = max( res, r - l + 1) # comapre prior max with current window size
        return res
