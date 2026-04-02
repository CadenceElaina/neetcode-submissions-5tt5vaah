class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # loop through the  string
        # track index of character until we reach a repeated character
        # use a set and clear the set after youve calculated the length of that set of characters?
        # or find the new start and end - r
        start = 0
        end = sys.maxsize
        max_len = 0

        char_map = {} # 0 - 25 characters
        char_set = set()
        for i, c in enumerate(s):
            if c in char_map:
                start = max(start, char_map[c] + 1)
            char_map[c] = i    
            curr_len = i - start + 1
            max_len = max(max_len, curr_len)
            char_set.add(c)

                        #while c not in char_set:
            # we know we reached a duplicate - set start to prior index of of character in map
            # only move if the duplicate is in our current window 

           #start = char_map[c]

        return max_len

            