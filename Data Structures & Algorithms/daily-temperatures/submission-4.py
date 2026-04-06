class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) # number of days for each index until the next warmer day

        for i, temp in enumerate(temperatures):
            # push values onto our stack
            # 30 - push 0
            #  stack and 30 < 38 - pop is our index and update result at that index with our outer loops i - the index in our stack
            # 38 - push 1
            # 30 - push 2
            # 36 > 30 (our last value in stack) so pop it get index and at that index we substract our stack index from our curr idx
            # 3-2=1 and if we move 1 from 30 we get a higher temp
            # !(36 > 38) so just push 3 onto our sttack: 1 (38), 3 (36)
            # 35 < 36 - append 4
            # 40 > 35 - pop 4 add 5-4 = 1 to res at that index (4) 
            # 40 > 36 - pop 3 add 5-3 = 2 at res[3]
            # 40 > 38 - pop 1 add 5-1 = 5 at res[1]
            # stack is empty - append 5
            # !(28 > 40): and we have no more values so just append our stack and were done - default values work for the values in our stack which is 0
            # res=[1, ]
            while stack and temperatures[stack[-1]]  < temp:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res