class Solution:
    # 3024. 三角形类型
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c  = nums
        if a + b <= c:
            return "none"
        if a == c:
            return "equilateral"
        if a == b or b == c:
            return "isosceles"
        return "scalene"