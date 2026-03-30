class Solution:
    # Strings can be any of the 256 ASCII chars (commas, spaces, etc.) - how do you determine whats apart of the word vs a separator?
    # where does one string end and the next begin?
    # prefix each string with its length - tell decoder exact length of str so it knows 
    # []"Hello", "World"] -> "5#Hello5#World"
    # we know # prefaces the start of the word and the index behind # is the length of the word
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # length of word + delimiter "#" + word
            result += str(len(s)) + "#" + s
        return result
    def decode(self, s: str) -> List[str]:
        # declare result array and pointer
        result, i = [], 0

        while i < len(s):
            # Find the delimeter to know where the length ends
            j = i
            while s[j] != "#":
                j += 1 #continue until we reach the delimiter
            
            length = int(s[i:j]) # get length of string from the starting pointer i until j which is the next #

            #Extract string using its length from j + 1 (first letter of str) until we reach end of length from start of str
            result.append(s[j + 1 : j + 1 + length])

            # Have to update pointer of i so that its pointing to the next #  or encoded str/segment
            i = j + 1 + length
        return result