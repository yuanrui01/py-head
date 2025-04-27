class Solution:
    # 3392. 统计符合条件长度为 3 的子数组数目
    def countSubarrays(self, nums: List[int]) -> int:
        return sum((nums[i-2] + nums[i]) * 2 == nums[i-1] for i in range(2, len(nums)))