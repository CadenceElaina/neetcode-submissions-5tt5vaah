class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for i, n in enumerate(s):
            hm1[n] = hm1.get(n, 0)+1
        for i, n in enumerate(t):
            hm2[n] = hm2.get(n,0)+1
        return hm1==hm2