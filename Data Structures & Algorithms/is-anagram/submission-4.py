class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        for char in s:
            if char in str1:
                    #uniqueChars.update({char: uniqueChars.get(char, 0) +1}) or:
                str1[char] = str1.get(char, 0) + 1
            else:
                str1[char] = 1

        str2 = {}
        for char in t:
            if char in str2:
                str2[char] = str2.get(char, 0) + 1
            else:
                str2[char] = 1
        return str1 == str2
    #print(str1)
    #print(str2)
