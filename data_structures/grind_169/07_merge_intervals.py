'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        intervals.sort(key = lambda x:x[0])

        merged = []
        current_interval = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            current_start, current_end = current_interval

            if start <= current_end:
                current_interval[1] = max(current_end, end)
            else:
                merged.append(current_interval)
                current_interval = interval
        
        merged.append(current_interval)

        return merged




        