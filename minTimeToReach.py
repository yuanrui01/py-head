class Solution:
    # 3341. 到达最后一个房间的最少时间 I
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        t = [[inf] * m for _ in range(n)]
        t[0][0] = 0
        h = [(0, 0, 0)]
        while True:
            time, x, y = heappop(h)
            if x == n - 1 and y == m - 1:
                return time
            if time > t[x][y]:
                continue
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    nt = max(time, moveTime[nx][ny]) + 1
                    if nt < t[nx][ny]:
                        t[nx][ny] = nt
                        heappush(h, (nt, nx, ny))