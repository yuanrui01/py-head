class Solution:
    # 1957. 删除字符使字符串变好
    def makeFancyString(self, s: str) -> str:
        ans = []
        i, n := 0, len(s)
        while i < n:
            ch = s[i]
            cnt = 1
            ans.append(ch)
            while i+1 < n and s[i+1] == ch:
                i += 1
                cnt += 1
                if cnt < 3:
                    ans.append(ch)
            i += 1
        return "".join(ans)