class Solution:
    # 3423. 循环数组中相邻元素的最大差值
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = abs(nums[0] - nums[-1])
        for i in range(1, n):
            ans = max(ans, abs(nums[i] - nums[i-1]))
        return ans