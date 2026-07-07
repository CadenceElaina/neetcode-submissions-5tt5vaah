class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # ord(s[r]) - order('A') -> A=0
        count = {}
        res = 0
        l = 0
        # sliding window  | advance r - add value at r to our count hm - if we add a duplicate continue until we run out of k swaps
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) +1
            # Window Size - Count of Most Frequent = Number of Swaps Needed for window to be valid
            # 4 - (Y: 2) = 2 - need 2 swaps
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l +1) # choose max size between prior max and current window size
        return res
