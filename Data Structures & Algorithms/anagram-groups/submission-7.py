class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        # list  for each char a-z 0-25 to count occurances to create freq map for eaqch word 
        for w in strs:
            freq=[0]*26
            for c in w:
                index = ord(c) - ord('a') # results in 'a' being 0 and z being 25
                freq[index] += 1
            key = tuple(freq)
            res[key].append(w) # freq is key and key stores lists of words with that freq
        return list(res.values())
