import sys

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        
        dp[i][j]: means the number of vocation days in i city and j week
        We use the bottom up
        """
        n, k = len(flights), len(days[0])
        res = 0
        dp = [[0] * k for _ in range(n)]

        for j in range(k-1, -1, -1):
            for i in range(n):
                dp[i][j] = days[i][j]
                for p in range(n):
                    if (i == p or flights[i][p]) and j < k-1:
                        dp[i][j] = max(dp[i][j], dp[p][j+1] + days[i][j])
                if j == 0 and (i == 0 or flights[0][i]): # either city is 0 or we have the flights to city i from city 0
                    res = max(res, dp[i][0])
        return res

solution = Solution()
flights = [[0,1,1],[1,0,1],[1,1,0]]
days = [[1,3,1],[6,0,3],[3,3,3]]
print(solution.maxVacationDays(flights, days))

