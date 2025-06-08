class Solution:
    # 386. 字典序排数
    def dfs(self, num: int, mx: int, res: List[int]) -> None:
        if num > mx:
            return
        res.append(num)
        num *= 10
        for i in range(10):
            self.dfs(num + i, mx, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res