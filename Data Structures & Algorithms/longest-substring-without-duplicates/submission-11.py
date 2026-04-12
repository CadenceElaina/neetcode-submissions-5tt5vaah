class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # as we loop through we grow window
        # window is our current index - left pointer
        # hash set to check if the char is present in the window or not.
        # when we encounter a character at index r that is already present in the
        # window we shink the window by incrementing the l pointer until the window no longer contains any dups
        #also we remove characters from the hash set that are exclusded from teh window as the l pointer moves
        # at each iteration we update the result with the length of the current window r-l+1
        # if this len is > than current res
        mp={}
        l=0
        res=0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1,l)
            mp[s[r]] = r
            res = max(res, r-l+1)
    
        return res