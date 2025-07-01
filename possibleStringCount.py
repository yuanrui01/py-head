class Solution:
    # 3330. 找到初始输入字符串 I
    def possibleStringCount(self, word: str) -> int:
        ans, i, = 1, 0
        n = len(word)

        while i < n:
            cnt = 1
            x = word[i]
            while i + 1 < n and word[i + 1] == x:
                cnt += 1
                i += 1
            ans += cnt - 1
            i += 1
        return ans