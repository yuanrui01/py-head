from collections import Counter
from typing import List

class Solution:
    # 2610. 转换二维数组
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = Counter(nums)

        while any(count.values()):
            row = []
            for num in list(count.keys()):
                if count[num] > 0:
                    row.append(num)
                    count[num] -= 1
                    if count[num] == 0:
                        del count[num]
            ans.append(row)
        
        return ans