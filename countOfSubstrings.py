class Solution:
    def countOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ch = [[0] * 6 for _ in range(n + 1)]
        ac, ec, ic, oc, uc, fc = 0, 0, 0, 0, 0, 0
        for i in range(n):
            if s[i] == 'a':
                ac += 1
            elif s[i] == 'e':
                ec += 1
            elif s[i] == 'i':
                ic += 1
            elif s[i] == 'o':
                oc += 1
            elif s[i] == 'u':
                uc += 1
            else:
                fc += 1
            ch[i + 1][0] = ac
            ch[i + 1][1] = ec
            ch[i + 1][2] = ic
            ch[i + 1][3] = oc
            ch[i + 1][4] = uc
            ch[i + 1][5] = fc
        
        def check(l: int, r: int) -> bool:
            for i in range(5):
                if ch[r][i] - ch[l][i] == 0:
                    return False
            return ch[r][5] - ch[l][5] == k
        
        ans = 0
        for w in range(k + 5, n + 1):
            for i in range(n - w + 1):
                if check(i, i + w):
                    ans += 1
        
        return ans
        