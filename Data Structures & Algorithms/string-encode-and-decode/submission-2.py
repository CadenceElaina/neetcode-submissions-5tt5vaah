class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # length + delimiter + string
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 1. find the delimiter to know where the length ends
            # 1, 10, 100
            j = i
            while s[j] != "#":
                j += 1
            
            # 2. extract length
            length = int(s[i:j])

            # 3.  start of str is j + 1 and goes until start + length
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 4. move pointer to repeat steps on next slice of chars & the next str
            i = end
        return res