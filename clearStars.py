class Solution:
    # 3170. 删除星号以后字典序最小的字符串
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c == '*':
                for j in range(26):
                    if stacks[j]:
                        stacks[j].pop()
            else:
                stacks[ord(c) - ord('a')].append(i)
        return ''.join(s[i] for i in sorted(chain.from_iterable(stacks)))