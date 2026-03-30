class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsHashmap = defaultdict(list)

        for str in strs:
            # index 0 = "a" index 25 = "z"
            freqMapOfLetters = [0] * 26
            for char in str:
                # ord(char) gets the ASCII value ('a' is 97, 'b' is 98, ...)
                # subtracting ord('a') initial value / bound will return correct index between 0-25 of our curr char
                index = ord(char) - ord("a")
                freqMapOfLetters[index] += 1 # once we know the index our letter goes at we increase count of that letter  
            key = tuple(freqMapOfLetters) # unique key stored in hashmap to rep this specific freqMap / anagram
            anagramsHashmap[key].append(str) # had to be a tuple to be put in a dictionary in Python
        
        return list(anagramsHashmap.values()) # we need to return a list of lists .values() returns the hashmap as a list? within our outer list()

        # keep freq map that holds a list so that each key contains an array of all anagrams of that type in an array/list
        # need to remember:  
        #                                       hashmap = {[], [], ...}
        #                                       anagramsHashmap = defaultdict(list) --- type of dic that auto creates new list for any key that doesnt exist when accessed - this allows us to append values to the list without having to check if the key is already present, simplifying the process of grouping items
        #                                       freqCount = [0] * 26 - 0-25 = a-z
        #                                       use ASCII value of num minus value of "a" to get index in format of 0-25
        #                                       place character into appropriate index of our freqMap of chars 
        #                                       Once we have freq map of the word we can place it into the correct spot in our final hashmap
        #                                       Have to convert list to a tuple since dicts cant use lists as keys
        #                                       key = tupel(lettersCount)
        #                                       anagramsHashmap[key].append(word)
        #                                       return list(anagramsHashmap.values())
        # return [[anagram(s) type 1], [anagram(s) type 2], ... [anagram(s) type n]]
        # need a list within a hashmap so that we can add by freq count / each unique anagram
        # 0th index represents "a" and the 25th = "z"
        # can use ord(char) to get ASCII val 
        # index = ord(char) - ord("a") 
        
        #letterCount[index] += 1
        # Convert the list to a tuple so it can be a dictionary key (dicts cant use lists as keys)
        # key = tuple(letterCount)
        # Append original word to key for this words character freq count
        #anagramsHashmap[key].append(word)
        
        #return list(anagramsHashmap.values())
