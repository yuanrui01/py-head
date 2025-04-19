class Solution:
    # 2563. 统计公平数对的数目
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            l = bisect.bisect_left(nums, lower - x, 0, j)
            r = bisect.bisect_right(nums, upper - x, 0, j)
            ans += r - l
        return ans