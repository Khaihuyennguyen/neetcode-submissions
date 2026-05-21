"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []

        for i in intervals:
            start, end = i.start, i.end
            times.append((start, 1))
            times.append((end, -1))

        times.sort(key = lambda x : (x[0], x[1]))

        count = 0
        result = 0
        for t in times:
            count += t[1]
            result = max(result, count)
        return result