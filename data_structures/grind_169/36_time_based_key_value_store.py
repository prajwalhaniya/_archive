'''
https://leetcode.com/problems/time-based-key-value-store/description/
'''

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        pairs = self.store[key]
        index = bisect.bisect_right(pairs, (timestamp, chr(127)))

        if index == 0:
            return ""

        return pairs[index - 1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
