class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        suf_min = [0] * n
        suf_min[n-1] = nums[n-1]
        for i in range(n-2, 1, -1):
            suf_min[i] = min(suf_min[i+1], nums[i])

        ans = 0
        pre_max = nums[0]
        for i in range(1, n - 1):
            x = nums[i]
            if pre_max < x < suf_min[i+1]:
                ans += 2
            elif nums[i-1] < x < nums[i+1]:
                ans += 1

            pre_max = max(pre_max, x)
        return ans