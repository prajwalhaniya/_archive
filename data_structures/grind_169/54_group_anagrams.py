'''
https://leetcode.com/problems/group-anagrams/
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagrams = defaultdict(list)

        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)

        return list(anagrams.values())