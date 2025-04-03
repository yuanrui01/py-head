class Solution:
    # 2874. 有序三元组中的最大值 II
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        rm = [0] * (n-2)
        lm = [0] * (n-2)
        rm[n-3] = nums[n-1]
        lm[0] = nums[0]
        for i in range(n-2, 1, -1):
            rm[i-2] = max(rm[i-1], nums[i])
        for i in range(1, n-2, 1):
            lm[i] = max(lm[i-1], nums[i])
        for i in range(1, n-1, 1):
            ans = max(ans, (lm[i-1]-nums[i]) * rm[i-1])
        return ans