class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            freq = [0]*26
            for c in w:
                index = ord(c) - ord('a')
                freq[index] +=1
            key = tuple(freq)
            res[key].append(w)
        
        return list(res.values())