'''
https://leetcode.com/problems/combination-sum/description/
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        def backtrack(start, remaining, current_combination):
            if remaining == 0:
                result.append(current_combination[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break

                current_combination.append(candidates[i])
                backtrack(i, remaining - candidates[i], current_combination)
                current_combination.pop()

        backtrack(0, target, [])
        return result