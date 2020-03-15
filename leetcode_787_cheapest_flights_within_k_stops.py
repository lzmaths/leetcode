import sys, collections, heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(dict)
        for s, d, cost in flights:
            graph[s][d] = cost

        heap = [[0, src, K+1]]
        while heap:
            #print(heap)
            c, s, k = heapq.heappop(heap)
            if s == dst:
                return c
            if k:
                for d in graph[s]:
                    heapq.heappush(heap, [c + graph[s][d], d, k-1])
        return -1