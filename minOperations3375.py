class Solution:
    # 3375. 使数组的值全部为 K 的最少操作次数
    def minOperations(self, nums: List[int], k: int) -> int:
        mn = min(nums)
        if (mn < k):
            return -1
        return len(set(nums)) - (k == mn)