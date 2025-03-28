class Solution:
    # 2716. 最小化字符串长度
    def minimizedStringLength(self, s: str) -> int:
        # return len(set(s))
        mask = 0
        for c in s:
            mask |= 1 << (ord(c) - ord('a'))
        return mask.bit_count()