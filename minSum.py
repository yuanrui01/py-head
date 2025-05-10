class Solution:
    # 2918. 数组的最小相等和
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        rs1 = [0,0]
        rs2 = [0,0]
        for _, x in enumerate(nums1):
            rs1[0] += x
            if x == 0:
                rs1[1] += 1
        for _, x in enumerate(nums2):
            rs2[0] += x
            if x == 0:
                rs2[1] += 1
        minS1 = rs1[0] + rs1[1]
        minS2 = rs2[0] + rs2[1]
        if minS1 == minS2:
            return minS1
        if minS1 > minS2 and rs2[1] > 0:
            return minS1
        if minS2 > minS1 and rs1[1] > 0:
            return minS2
        return -1