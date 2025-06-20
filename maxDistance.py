class Solution:
    # 3443. K 次修改后的最大曼哈顿距离
    def maxDistance(self, s: str, k: int) -> int:
        nN, nS, nW, nE = 0, 0, 0, 0
        ans , absV, absH, ck = 0, 0, 0, 0
        for _, c in enumerate(s):
            if c == 'N':
                nN += 1
            elif c == 'S':
                nS += 1
            elif c == 'W':
                nW += 1
            else:
                nE += 1
            absV = abs(nN - nS)
            absH = abs(nW - nE)
            ck = min(k, min(nN, nS) + min(nW, nE))
            ans = max(ans, absH + absV + 2 * ck)
        return ans