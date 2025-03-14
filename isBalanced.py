# 3340. 检查平衡字符串
class Solution:
    def isBalanced(self, num: str) -> bool:
        s = 0
        for i, c in enumerate(map(int, num)):
            s += c if  i % 2 else -c
        return s == 0