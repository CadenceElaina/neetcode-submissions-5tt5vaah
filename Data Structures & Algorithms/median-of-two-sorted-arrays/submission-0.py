class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A #swap

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  #pter for A
            j = half - i  - 2 # pter for B

            #left partition - if i is within bounds of A (0 - len(A)) then use i and i+1 for bounds
            # otherwise we use -inf for left bound and inf for right
            Aleft = A[i] if i >= 0 else float("-infinity")# i < 0? default val
            Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
            #right partition
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j + 1] if (j+1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0 #decimal division
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
            


        # z elements in both arrays
        # if z is odd med(x) = x(z+1) / 2
        # if z is even med(x) = [x(n/2) + x((n/2)+1) ] / 2

        # combining of arrays makes them unsorted! 

        #combinedLength = len(nums1) + len(nums2) 
       # median = 0
      #  if combinedLength % 2 != 0:
      #      return combined_arr[combinedLength // 2] # exactly in middle
  #      else:
     #       return (combined_arr[(combinedLength // 2) - 1] + combined_arr[combinedLength // 2]) / 2.0
        