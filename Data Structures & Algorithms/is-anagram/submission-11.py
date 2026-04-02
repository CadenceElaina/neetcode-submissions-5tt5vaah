class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # character freq map
        # key = a-z : value= count 
        s1freqmap={}
        for c in s:
            s1freqmap[c] = s1freqmap.get(c, 0) + 1
        s2freqmap={}
        for c in t:
            s2freqmap[c] = s2freqmap.get(c,0)+1
        
        return s1freqmap == s2freqmap