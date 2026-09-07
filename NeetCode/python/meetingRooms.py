"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start) # sorting with lambda 

        for i in range(1,len(intervals)):
            i1=intervals[i-1]#prev
            i2=intervals[i]#cur

            if i1.end>i2.start:
                return False

        return True
