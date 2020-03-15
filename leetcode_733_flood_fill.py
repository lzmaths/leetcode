import sys

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # DFS
        if not image or image[sr][sc] == newColor:
            return image

        self.dfs(sr, sc, image[sr][sc], newColor, image)
        return image

    def dfs(self, r, c, color, new_color, image):
        if image[r][c] != color:
            return
        image[r][c] = new_color
        m, n = len(image), len(image[0])
        for dx, dy in ([-1, 0], [1, 0], [0, -1], [0, 1]):
            nx = r + dx
            ny = c + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            self.dfs(nx, ny, color, new_color, image)
        