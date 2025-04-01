class Solution:
    # 2140. 解决智力问题
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        for i in range(n-1, -1, -1):
            p = questions[i][0]
            b = questions[i][1]
            dp[i] = p
            if (i + b + 1 < n):
                dp[i] += dp[i+b+1]
            if (i + 1 < n):
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]
