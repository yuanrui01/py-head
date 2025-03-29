class Solution:
    # 2360. 图中的最长环
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        n = len(edges)
        visTime = [0] * n
        curTime = 1
        for i in range(n):
            x = i
            startTime = curTime
            while x != -1 and visTime[x] == 0:
                visTime[x] = curTime
                curTime += 1
                x = edges[x]
            if x != -1 and visTime[x] >= startTime:
                ans = max(ans, curTime - visTime[x])
        return ans