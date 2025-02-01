'''
We're given an array of meeting intervals, intervals where intervals[i] = [start[i], end[i]]. 
We have to determine if a person can attend all meetings without any overlap. 
Return TRUE if possible, otherwise return FALSE.

https://www.educative.io/answers/meeting-rooms-leetcode
'''

def can_attend_meetings(intervals):
    
    intervals.sort(key=lambda x: x[0])
    
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i + 1][0]:
            return False
    
    return True