class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 # for each str get its freq map -> list where list is that freq of chars

        groups=defaultdict(list)
        # 
        for w in strs:
            freq = [0] * 26 # each index represents a-z
            for c in w:
                freq[ord(c) - ord('a')] += 1
            key = tuple(freq) # hashtable - keys need to be immutable - convert freq list to tuple
            groups[key].append(w)
        return list(groups.values())
