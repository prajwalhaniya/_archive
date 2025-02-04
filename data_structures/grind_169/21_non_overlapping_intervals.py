'''
https://leetcode.com/problems/non-overlapping-intervals

'''
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key = lambda x: x[1])

        count = 0
        last_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start < last_end:
                count += 1
            else:
                last_end = end

        return count

