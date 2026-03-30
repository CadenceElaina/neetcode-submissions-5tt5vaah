class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given array of ints
        # return result[] 
        # so probably need to sort array and use ... hmm 
        #Input: temperatures = [30,38,30,36,35,40,28]

        #Output: [1,4,1,2,1,0,0]
        # so 38 -> 40 = 4 inclusive of 40s index
        # i feel lik you could do two pointer strat here as well idk
        # but obv we use a stack since this question is under stacks 
        # one stack to track values until we reach the next highest value after our current value or if there is no value ahead that is larger place a 0 at that index
        # loop through list for each index loop until you find a larger value - O(n^2) brute force
        # how do we loop through only once and track this...
        # 
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res

            
