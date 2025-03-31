class Solution:
    # 2278. 字母在字符串中的百分比
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = 0
        n = len(s)
        for i in range(n):
            if (s[i] == letter):
                cnt += 1
        return int(100.0 * cnt / n)