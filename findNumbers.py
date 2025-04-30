class Solution:
    # 1295. 统计位数为偶数的数字
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            while x >= 100:
                x /= 100
            if x >= 10:
                ans += 1
        return ans