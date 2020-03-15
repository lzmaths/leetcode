import collections

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        reach = [[0] * n for _ in range(m)]
        distance = [[0] * n for _ in range(m)]
        bld_cnt = 0
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bld_cnt += 1
                    q.append((i, j, 0))
                    visited = set()
                    while q:
                        curr = q.popleft()
                        x, y = curr[0], curr[1]
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x+dx, y+dy
                            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited and grid[nx][ny] == 0:
                                reach[nx][ny] += 1
                                q.append((nx, ny, curr[2] + 1))
                                visited.add((nx, ny))
                                distance[nx][ny] += curr[2] + 1
        res = float('inf')
        for i in range(m):
            for j in range(n):
                if reach[i][j] == bld_cnt:
                    res = min(res, distance[i][j])

        return res if res != float('inf') else -1
