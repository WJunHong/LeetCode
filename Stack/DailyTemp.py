class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        else:
            stack = []
            res = [0] * len(temperatures)
            for i in range(0, len(temperatures)):
                while len(stack) > 0 and temperatures[stack[len(stack) - 1]] < temperatures[i]:
                    res[stack[len(stack) - 1]] = i - stack[len(stack) - 1]
                    stack.pop()
                stack.append(i)
            return res

# Stack lower temperatures
# Pop from stack once higher temp achieved, keep popping and updating their values
