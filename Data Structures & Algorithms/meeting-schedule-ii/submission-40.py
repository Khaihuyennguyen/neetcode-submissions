"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # if we have a way to sort the meetings
        # based on their start time we will know the order of the next room should be
        # then we have a data structure that can store the end time work with this rule
        # we go thought the sorted meeting then we compare the current start time with the earliest end time if the start time is less than the end time we need one more room 
        # we add that of course it priority the end time so we always have the earlist ending time

        # 0 40, 5 10, 15 20
        # 10, 40
        # becase 15 is larger than 10, so we can reuse that room
        # 20, 40
        heap = []
        intervals.sort(key = lambda x: x.start)


        for i in range(len(intervals)):
            if heap and  intervals[i].start >= heap[0]:
                heapq.heappop(heap)
           
            heapq.heappush(heap, intervals[i].end)

        return len(heap)