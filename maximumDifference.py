class Solution:
    # 2016. 增量元素之间的最大差值
    def maximumDifference(self, nums: List[int]) -> int:
        ans, mn = -1, nums[0]
        for _, x in enumerate(nums):
            if (x > mn):
                ans = max(ans, x - mn)
            mn = min(mn, x)
        return ans
