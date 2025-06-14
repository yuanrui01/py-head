class Solution:
    # 2566. 替换一个数字后的最大差值
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        firstNot9 = '.'
        firstC = s[0]
        for c in s:
            if c != '9':
                firstNot9 = c
                break
        mx, mn = 0, 0
        for i, c in enumerate(s):
            mx = mx * 10 + (9 if c == firstNot9 else int(c))
            mn = mn * 10 + (0 if c == firstC else int(c))
        return mx - mn