import sys
import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int

        The idea is to use mini_heap:
        - first sort the intervals by the starting time
        - compare the top of heap and curr starting time
          and heap push the ending time to the mini heap, 
        
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        ans = 0
        for interval in intervals:
            if len(heap) == 0:
                heapq.heappush(heap, interval[1])
                ans = max(ans, len(heap))
                continue
            top = heapq.heappop(heap)
            if top > interval[0]:
                heapq.heappush(heap, top)
            heapq.heappush(heap, interval[1])
            ans = max(ans, len(heap))

        return ans

solution = Solution()
intervals = [[0, 30],[5, 10],[15, 20]]
print(solution.minMeetingRooms(intervals))

intervals = [[[7,10],[2,4]]]
print(solution.minMeetingRooms(intervals))
