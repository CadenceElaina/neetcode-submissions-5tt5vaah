class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
        
        # window is fixed to length of s1. Could check every combo in that length or we can identify 
        # keep track with hash map for what we need vs what we have update as window moves
        # if we contain the letters we need in that window we return true
        hm = {}
        for c in s1:
            hm[c]=hm.get(c,0)+1


        s2hm={}


        for r in range(len(s2)):
            # add char from right
            char_in = s2[r]
            s2hm[char_in] = s2hm.get(char_in,0)+1

            if r >= len(s1):
                char_out = s2[r-len(s1)] # remove
                if s2hm[char_out] == 1:
                    del s2hm[char_out]
                else:
                    s2hm[char_out] -= 1
            if s2hm==hm:
                return True

        return False

       # for i, c in enumerate(s2):
         #   l = 0
          #  r=i
          #  if c in hm:
           #     s2hm[c]=s2hm.get(c,0)+1
             #   if s2hm == hm:
                #    return True
                
