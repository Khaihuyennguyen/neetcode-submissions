class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        previousEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < previousEnd:
                res += 1
                previousEnd = min(end, previousEnd)
            else:
                previousEnd = end
        return res
