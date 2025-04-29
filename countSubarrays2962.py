from typing import List


class Solution:
    # 2962. 统计最大元素出现至少 K 次的子数组
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        mxCnt = ans = left = right = 0

        while right < n:
            if nums[right] == mx:
                mxCnt += 1
            while mxCnt >= k:
                ans += n - right
                if nums[left] == mx:
                    mxCnt -= 1
                left += 1
            right += 1
        return ans