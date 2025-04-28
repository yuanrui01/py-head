class Solution:
    # 1399. 统计最大组的数目
    def countLargestGroup(self, n: int) -> int:
        def getSum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        cnt = [0] * 37
        for i in range(1, n + 1):
            ds = sum(map(int, str(i)))
            cnt[ds] += 1
        return cnt.count(max(cnt))
