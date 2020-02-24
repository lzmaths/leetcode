class Solution:
    """
    https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/409009/JavaC%2B%2BPython-DP-Solution
    """
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit), key=lambda v: v[0])
        dp = [[0, 0]]
        for e, s, p in jobs:
            pos = bisect.bisect_right(dp, [s+1])-1
            if dp[pos][1] + p > dp[-1][1]:
                dp.append([e, dp[pos][1] + p])
            print(e, s, p, dp, pos)
        return dp[-1][1]
        
