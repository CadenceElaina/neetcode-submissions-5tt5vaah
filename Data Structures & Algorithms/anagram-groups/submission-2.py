class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsHashmap = defaultdict(list)

        for str in strs:
            freqmapOfChars = [0] * 26
            for char in str:
                index = ord(char) - ord("a") # returns 0-25 if provided vals a-z and 0 represents "a" 25 = "z" in our list
                freqmapOfChars[index] += 1
            key = tuple(freqmapOfChars)
            anagramsHashmap[key].append(str) # key is our freqmap of chars and val is our string we just counted chars of
        
        return list(anagramsHashmap.values())

