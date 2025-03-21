from typing import List

class Solution:
    # 2643. 一最多的行
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0, 0]
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            cnt = 0
            for j in range(m):
               cnt += mat[i][j]
            if cnt > ans[1]:
                ans = [i, cnt]
        return ans