class Solution:
    # 2302. 统计得分小于 K 的子数组数目
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum = count = left = right = 0
        n = len(nums)

        while right < n:
            sum += nums[right]
            while left <= right and sum * (right - left + 1) >= k:
                count += (n - right)
                sum -= nums[left]
                left += 1
            right += 1
        return n * (n + 1) // 2 - count