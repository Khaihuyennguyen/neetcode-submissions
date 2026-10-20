class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0

        intervals.sort()
        previousEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < previousEnd:
                count += 1
                previousEnd = min(previousEnd, intervals[i][1])
            else:
                previousEnd = intervals[i][1]
        return count
