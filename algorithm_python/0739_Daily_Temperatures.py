class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # stack - monotonic decreasing
        # backwards
        length = len(temperatures)
        ans = [0] * length
        stack = [] # store index instead of value
        for i in range(length - 1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            ans[i] = (stack[-1] - i) if stack else 0
            stack.append(i)

        return ans