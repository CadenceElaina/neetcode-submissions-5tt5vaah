class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq map of chars of each string -> stored in a hashmap  - where the values are lists of each word
        anagramsHashmap = defaultdict(list) #k:v v=[]
        
        for s in strs:
            freqMapOfChars = [0] * 26 # each pos represents a-z - 0=a 1=b ... 26=z
            for c in s:
                # need to get index to add to - 
                # python ord() function returns the Unicode code of a given single character
                index = ord(c) - ord("a") # a is our starting bound such that ord(a) - ord(a) = 0 
                freqMapOfChars[index] +=1
            key = tuple(freqMapOfChars) # dictionaries in python cannot hold lists as keys but can use tuples
            #bc keys are immutable and so are tuples! but not lists :c
            anagramsHashmap[key].append(s) # add our string to the appropriate key in our hashmap
        return list(anagramsHashmap.values())