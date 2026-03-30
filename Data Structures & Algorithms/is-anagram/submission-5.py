class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        for char in s:
            str1[char] = str1.get(char, 0) + 1

        str2 = {}
        for char in t:
            str2[char] = str2.get(char, 0) + 1

        return str1 == str2
