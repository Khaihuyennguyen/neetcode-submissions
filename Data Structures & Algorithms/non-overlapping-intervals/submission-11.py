class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        previousEnd = intervals[0][1]
        res = 0
        for i in range(1, len(intervals)):
            if previousEnd > intervals[i][0]:
                res += 1
                previousEnd = min(previousEnd, intervals[i][1])
            else:
                previousEnd = intervals[i][1]
        return res
