class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        s1hm = {}
        for c in s1:
            s1hm[c] = s1hm.get(c, 0) +1
        
        s2hm={}
        for r in range(len(s2)):
            s2hm[s2[r]] = s2hm.get(s2[r], 0)+1
            # is r >= len(s1)? then we must remove the leftmost char from our freq map of current window
            if r >= len(s1):
                #  s1="ab" s2="bcadba" --- len(s1) == 2
                # r = 0 s2hm={"b":1} -> r = 1 s2hm={"b":1, "c":1} -> r=2 s2hm={"b":1, "c":1, "a": 1} , 2>=2? -> yes remove a char
                # r = 2, len(s1) = 2 --- 2-2 = 0 ---> remove s2[0] "b"
                # update the freq map so that "b" occurrences is decremented by 1 but if "b" has only 1 occurrence then we must remove it from the hm since a value occur 0 times isnt necessary to track
                char_out = s2[r-len(s1)]
                if s2hm[char_out] == 1:
                    del s2hm[char_out]
                else:
                    s2hm[char_out]-=1
            if s2hm == s1hm:
                return True
        return False

        
