class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0] )
        # if the current start < previousEnd => return False
        output = [intervals[0]]

        for start, end in intervals:
            previousEnd = output[-1][1]
            if start > previousEnd:
                output.append([start, end])
            else:
                output[-1][1] = max(previousEnd, end)
        return output

