class Solution:
    # 2873. 有序三元组中的最大值 I
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)          
        for i in range(n-2):
            for j in range(i+1, n-1, 1):
                if (nums[i] > nums[j]):
                    for k in range(j + 1, n, 1):
                        ans = max(ans, (nums[i] - nums[j]) * nums[k])
        return ans