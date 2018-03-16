# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __str__(self):
        return '[{},{}]'.format(self.start, self.end)

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # sorted(intervals, key=)
        intervals.sort(key = lambda i:i.start)
        ret = []
        for i in intervals:
            if len(ret)==0 or ret[-1].end < i.start:
                ret.append(i)
            else:
                ret[-1].end = i.end
        return ret

if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1,3),Interval(2,6),Interval(8,10),Interval(15,18),Interval(0,0)]
    result = solution.merge(intervals)
    for i in result:
        print(i, end=' ')
    print()