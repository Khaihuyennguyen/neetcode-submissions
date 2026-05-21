class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            previousEnd = result[-1][1]
            if previousEnd >= start:
                result[-1][1] = max(end, previousEnd)
            else:
                result.append([start, end])
        
        return result