class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window can never exceed k replacements
        # 26 A-Z
        # windowLen - count [char] = k use needs to be <= k
        # which char is most freq? 
        # start at beg expand as much as possible - shift until valid
        # LR at beg
        # counts are zero
        # ABABBA k=2
        # l, r = 0
        # r+1 r+1 r+1 update counts A:1, B:1, A:2, B:2, B:3, A:3 
        # 6 len - 3 (freq of B and A) = 3 <= k? not valid -> shrink size of window until valid
        # l+1 and A is reduced to 2 ... 5-3 = 2 <= k - valid res = 5 right pointer cant be shifted more done
        # res updates as you go

        # maxf = 3 .... length - maxf - if you find a more freq char we dont care about the old maxf or updating them
         

        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
             # window = r-l +1 (not zero indexed). Subtracting the value of largest freq tells us k
             # if <= k its valid otherwise we must increment l and 
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res