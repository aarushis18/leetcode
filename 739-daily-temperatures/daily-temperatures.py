class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)               # array with final number of days
        mono = []                                   # store indices of the temperature array

        for ind, temp in enumerate(temperatures):
                while mono and temperatures[mono[-1]] < temp:   # temp is increasing
                    prev_ind = mono.pop()
                    ans[prev_ind] = ind - prev_ind
                
                mono.append(ind)                    # append the current index to the stack

        return ans