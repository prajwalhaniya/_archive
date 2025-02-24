'''
https://leetcode.com/problems/ransom-note/
'''

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magzine_counts = Counter(magazine)
        ransom_counts = Counter(ransomNote)

        for char, counts in ransom_counts.items():
            if magzine_counts[char] < counts:
                return False

        return True


        