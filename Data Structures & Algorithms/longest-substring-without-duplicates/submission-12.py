class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet: # if the current letter is in our char set keep removing from left until we no longer have a duplicate
                charSet.remove(s[l])
                l += 1 # advance left pointer until we no longer have dups
            charSet.add(s[r]) # once safe to add r without it being a dup do so
            res = max(res, r - l + 1)
        return res
