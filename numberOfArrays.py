from itertools import accumulate


class Solution:
    # 2145. 统计隐藏数组数目
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_s = min(accumulate(differences, initial=0))
        max_s = max(accumulate(differences, initial=0))
        return max(0, upper - lower - (max_s - min_s) + 1)