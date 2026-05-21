"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        schedules = []

        for i in intervals:
            start, end = i.start, i.end
            schedules.append((start, 1))
            schedules.append((end, -1))

        schedules.sort(key=lambda x: (x[0], x[1]))

        count = 0

        maxCount = 0

        for i in schedules:
            count += i[1]
            maxCount = max(maxCount, count)
        return maxCount