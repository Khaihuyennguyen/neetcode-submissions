class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        count = 0

        previousEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= previousEnd:
                previousEnd = end
            else:
                count += 1
                previousEnd = min(end, previousEnd)
        return count
        