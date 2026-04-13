class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #list where each index represents a letter a - z from 0-25 and increment count at each index
        res = defaultdict(list)
        for w in strs:
            freq = [0] *26
            for c in w:
                index = ord(c) - ord('a')
                freq[index] += 1
            key = tuple(freq)
            res[key].append(w)
        return list(res.values())
            