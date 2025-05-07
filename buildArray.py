
from typing import List


class Solution:
    # 1920. 基于排列构建数组
    def buildArray(self, nums: List[int]) -> List[int]:
        for i, x in enumerate(nums):
            if x < 0:
                continue
            cur = i
            while nums[cur] != i:
                nxt = nums[cur]
                nums[cur] = ~nums[nxt]
                cur = nxt
            nums[cur] = ~x
        for i, x in enumerate(nums):
            nums[i] = ~x
        return nums