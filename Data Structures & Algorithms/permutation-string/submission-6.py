class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #fixed-size sliding window with a frequency map.
        s1Len, s2Len = len(s1), len(s2)
        if s1Len > s2Len:
            return False
        s1_counts = [0] * 26 
        s2_counts = [0]*26


        #s1Len = len(s1)
        # populate values for our first window in s1 and s2 counts
        for i in range(s1Len):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1 
        
        # Check the initial window first before sliding
        if s1_counts == s2_counts:
            return True
        
        # Start at index after our first window ends
        for i in range(s1Len, s2Len):
            # add newest value at end of our window
            s2_counts[ord(s2[i]) - ord('a')] += 1 # Update happens second
            s2_counts[ord(s2[i - s1Len]) - ord('a')] -=1
            if s1_counts == s2_counts:
                return True
        return False