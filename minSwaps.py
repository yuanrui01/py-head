class Solution:
    # 1963. 使字符串平衡的最小交换次数
    def minSwaps(self, s: str) -> int:
        s = list(s)
        ans = c = 0
        j = len(s) - 1
        for b in s:
            if b == '[':
                c += 1
            elif c > 0:
                c -= 1
            else:
                while s[j] == ']':
                    j -= 1
                s[j] = ']'
                ans += 1
                c += 1

        return ans