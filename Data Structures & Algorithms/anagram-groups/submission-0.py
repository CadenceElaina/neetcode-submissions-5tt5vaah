class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using defaultdict(list) means if a key doesn't exist,
        # it automatically creates an empty list [] for us.
        anagramsHashmap = defaultdict(list)  # initialize hashmap/dictionary with {[]}
        for word in strs:
            # 0th index represents "a" and 25th = "z"
            lettersCount = [0] * 26
            for char in word:
                # loop through string and add count to correct index for the current char

                # ord(char) gets the ASCII value (e.g., 'a' is 97, 'b' is 98)
                # Subtracting ord('a') maps 'a' -> 0, 'b' -> 1, ..., 'z' -> 25
                index = ord(char) - ord("a")
                lettersCount[index] += 1
            # Convert the list to a tuple so it can be a dictionary key (dicts cant use lists as keys)
            key = tuple(lettersCount)
            # Append original word to key for this words character frequency count
            anagramsHashmap[key].append(word)

        return list(anagramsHashmap.values())