class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            length = str(len(s))
            result+= length+"#"+s
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1 # represents index 
            
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length]) 
            i = j + 1 + length
        return result