class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]

            while stack and t > stack[-1][1]:
                stack_i, stack_t = stack.pop()
                res[stack_i] = i - stack_i
            
            else:
                stack.append((i, t))
        return res


# 30, 25, 35
# 0, 1, 2
# 0, 0, 0