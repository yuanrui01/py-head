class Solution:
    # 2712. 使所有字符相等的最小成本
    def minimumCost(self, s: str) -> int:
        n = len(s)
        if ( n == 1):
            return 0
        ans0 = ans1 = 0
        b0 = b1 = False

        for i in range(n//2 -1, -1, -1):
            if ((s[i] == '0' and not b1) or  (s[i] == '1' and b1)):
                ans1 += i + 1
                b1 = not b1
        
            if ((s[i] == '1' and not b0) or (s[i] == '0' and b0)):
                ans0 += i + 1
                b0 = not b0
        
        b0 = b1 = False

        for i in range(n // 2, n):
            if ((s[i] == '0' and not b1) or  (s[i] == '1' and b1)):
                ans1 += n - i
                b1 = not b1
        
            if ((s[i] == '1' and not b0) or (s[i] == '0' and b0)):
                ans0 += n - i
                b0 = not b0

        return min(ans0, ans1)
    

solution = Solution()
print(solution.minimumCost("010101"))