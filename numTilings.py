MOD = 10**9 + 7

class Solution:
    # 790. 多米诺和托米诺平铺
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = (f[i - 3] + f[i - 1] * 2) % MOD
        return f[n]