class Solution:
    # 2138. 将字符串拆分为若干长度为 k 的组
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        return [s[i:i + k] + fill * (k - n + i) for i in range(0, n, k)]