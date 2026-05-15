class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of freq of chars 
        # if exceeds k then shrink window from left side 
        # is valid: r-l + 1> k?
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l +1)
        return res