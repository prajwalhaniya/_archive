'''
https://leetcode.com/problems/longest-common-prefix/submissions/1560452235/
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""


        reference = strs[0]

        for i in range(len(reference)):
            char = reference[i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != char:
                    return reference[:i]

        return reference