class Solution:
    # 3355. 零数组变换 I
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0 ] * (n + 1)
        for _, q in enumerate(queries):
            diff[q[0]] += 1
            diff[q[1] + 1] -= 1
        for i in range(n):
            if nums[i] > diff[i]:
                return False
            diff[i+1] += diff[i]
        return True