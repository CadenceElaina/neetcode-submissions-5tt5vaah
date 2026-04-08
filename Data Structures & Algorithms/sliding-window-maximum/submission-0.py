class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() # Stores indices
        l = r = 0

        while r < len(nums):
            # 1. Maintain monotonic property: 
            # Remove smaller values from the back because they'll never be the max
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            # 2. Clean up: 
            # Remove the index from the front if it has fallen out of the window range
            if l > q[0]:
                q.popleft()

            # 3. Collect Result:
            # Once the window reaches size k, append the max (the front of our deque)
            if (r + 1) >= k:
                # We append nums[q[0]] because q[0] is the index of the max value
                output.append(nums[q[0]])
                l += 1
            
            r += 1
            
        return output