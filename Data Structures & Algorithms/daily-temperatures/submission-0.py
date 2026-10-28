class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #[[temp, idx]]
        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                res[stack_i] = i - stack_i
            stack.append([t,i])
        return res
