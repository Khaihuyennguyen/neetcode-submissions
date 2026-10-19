class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 1, 2, 3 ,6 ,7, 8

        # check for each interval if that query inside that interval
        # if it is inside that interval: we add that interval inside by adding the shortest length and the last element (so we know where it end)
        # if the query not inside that : we keep removing 

        res = {}
        i = 0

        intervals.sort()
        minHeap = []
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]