class Solution:
    # 2294. 划分数组使最大差为 K
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = index = 0
        rem = k
        while index < n:
            while index + 1 < n and nums[index + 1] - nums[index] <= rem:
                rem -= nums[index+1] - nums[index]
                index += 1
            index += 1
            ans += 1
            rem = k
        return ans