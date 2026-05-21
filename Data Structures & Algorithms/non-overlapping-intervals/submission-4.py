class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        previousEnd = intervals[0][1]

        count = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start >= previousEnd:
                previousEnd = end
            else:
                count += 1
                previousEnd = min(previousEnd, end)
        return count
        