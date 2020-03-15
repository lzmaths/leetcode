class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = []
        cols = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)
        
        cols.sort()
        #print(rows, cols)
        ans = 0
        i, j = 0, len(rows)-1
        while i < j:
            ans += rows[j] - rows[i] + cols[j] - cols[i]
            i += 1
            j -= 1
        return ans