class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for i, c in enumerate(s):
            s1[c] = s1.get(c, 0 )+1
            if i < len(t):
                s2[t[i]] = s2.get(t[i], 0)+1
            if i == len(s)-1 and len(s) < len(t):
                count = i
                while  count < len(t):
                    s2[t[i]] = s2.get(t[i], 0)+1
                    count+=1
   
        
        return s1 == s2