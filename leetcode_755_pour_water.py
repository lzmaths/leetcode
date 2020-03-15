import sys


class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if K == 0:
            return heights
        for _ in range(V):
            r = K
            while r < len(heights)-1 and heights[r] >= heights[r+1]:
                r += 1
            while r > K and heights[r-1] == heights[r]:
                 r -= 1
            
            l = K
            while l > 0 and heights[l] >= heights[l-1]:
                l -= 1
            while l < K and heights[l+1] == heights[l]:
                l += 1
            if heights[l] < heights[K]:
                heights[l] += 1
            else:
                heights[r] += 1
        return heights