class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq map of chars
        # store freq map as a key 
        # keys may contain a list of words that are that anagram
        # skip index 0

        res = defaultdict(list)
        # list each char a-z 0-25 to help build a freq map for each word
        for w in strs:
            freq=[0]*26
            for c in w:
                l = ord(c) - ord('a')
                freq[l] += 1
            key = tuple(freq)
            res[key].append(w) # freq is key and key stores lists of words with that freq
        return list(res.values())