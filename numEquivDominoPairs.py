class Solution:
    # 1128. 等价多米诺骨牌对的数量
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        flag = [[1] * 10 for _ in range(10)]
        count = [[0] * 10 for _ in range(10)]
        for i in range(len(dominoes)):
            a, b = dominoes[i]
            count[a][b] += 1
        for i in range(10):
            for j in range(10):
                c = 0
                if flag[i][j]:
                    flag[i][j] = 0
                    c += count[i][j]
                if flag[j][i]:
                    flag[j][i] = 0
                    c += count[j][i]
                if c > 1:
                    ans += c * (c - 1) // 2
        return ans