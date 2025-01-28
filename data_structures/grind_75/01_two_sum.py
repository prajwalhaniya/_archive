'''
https://leetcode.com/problems/two-sum/

Input: nums = [3,2,4], target = 6
Output: [1,2]
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            num_to_index[num] = index
        
        return []