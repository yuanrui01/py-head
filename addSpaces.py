class Solution:
    # 2109. 向字符串添加空格
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        n = len(s)
        m = len(spaces)
        j = 0
        for i in range(n):
            if j < m and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(s[i])
        return ''.join(ans)