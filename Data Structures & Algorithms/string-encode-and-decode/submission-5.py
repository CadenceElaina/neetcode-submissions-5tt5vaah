class Solution:

    def encode(self, strs: List[str]) -> str:
        # loop over strings add len of string + delimiter then string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # j stopped at # so get string which is from j+1 to j+1+length (len of curr str)
            i = j + 1 + length
        return res
     #   for i, c in enumerate(s):
            # proceed until # once hash get chars before hash which is the lenght of the str
            # while 
        #    while c != "#":
         #       length += c
            #length = int(length)