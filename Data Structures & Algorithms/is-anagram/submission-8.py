class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # character freq map
        # key = a-z : value= count 
        str1 = {}
        for char in s:
            # check if we've added this letter if so increase count otherwise set = 0 then increase by 1
            str1[char] = str1.get(char, 0) + 1
            
        str2 = {}
        for char in t:
            str2[char] = str2.get(char, 0) + 1
            
        return str1 == str2
