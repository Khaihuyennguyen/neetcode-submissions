class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])

        res = []
        previous = intervals[0][1]

        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < previous:
                count += 1
                previous = min(previous, intervals[i][1])
            else:
                previous = intervals[i][1]
            
        return count

