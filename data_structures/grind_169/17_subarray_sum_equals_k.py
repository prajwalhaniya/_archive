'''
https://leetcode.com/problems/subarray-sum-equals-k
'''

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum_counts = { 0: 1 }
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            if (prefix_sum - k) in prefix_sum_counts:
                count += prefix_sum_counts[prefix_sum - k]

            if prefix_sum in prefix_sum_counts:
                prefix_sum_counts[prefix_sum] += 1
            else:
                prefix_sum_counts[prefix_sum] = 1

        return count 