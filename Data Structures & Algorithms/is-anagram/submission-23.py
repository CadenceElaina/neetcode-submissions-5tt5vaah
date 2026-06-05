class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if not(len (s) == len(t)):
        return False
      s1 = {}
      s2 = {}
      for c in s:
        s1[c] = s1.get(c, 0) + 1
      for z in t:
        s2[z] = s2.get(z,0)+1
      return s1 == s2

        