import sys

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        k = 10
        visited = [False] * k
        jumps = [[0] * k for _ in range(k)]
        jumps[1][3] = jumps[3][1] = 2
        jumps[4][6] = jumps[6][4] = 5
        jumps[7][9] = jumps[9][7] = 8
        jumps[1][7] = jumps[7][1] = 4
        jumps[2][8] = jumps[8][2] = 5
        jumps[3][9] = jumps[9][3] = 6
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 5

        res = 0
        res += self.helper(1, 1, m, n, jumps, visited, 0) * 4
        res += self.helper(2, 1, m, n, jumps, visited, 0) * 4
        res += self.helper(5, 1, m, n, jumps, visited, 0)

        return res


    def helper(self, num, curr_len, m, n, jumps, visited, res):
        if curr_len >= m:
            res += 1
        curr_len += 1
        if curr_len > n:
            return res
        visited[num] = True
        for next in range(1, 10):
            jump = jumps[num][next]
            if not visited[next] and (jump == 0 or visited[jump]):
                res = self.helper(next, curr_len, m, n, jumps, visited, res)

        visited[num] = False

        return res
