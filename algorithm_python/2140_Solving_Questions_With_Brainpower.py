class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        memo = {}
        def dp(i):
            nonlocal memo, questions
            # def: return most points in [i, end]
            # base case (at end)
            if i >= len(questions):
                return 0
            # memo
            if i in memo:
                return memo[i]
            # recurrence relation
            j = i + questions[i][1] + 1
            memo[i] = max(questions[i][0] + dp(j), dp(i + 1))
            # ans
            return memo[i]
            
        return dp(0)