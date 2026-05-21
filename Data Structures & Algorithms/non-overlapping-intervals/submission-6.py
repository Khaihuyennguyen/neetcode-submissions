class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1   2
        #     2   3
        # 1         4

        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res