'''
https://leetcode.com/problems/move-zeroes
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_ptr] = nums[i]
                non_zero_ptr += 1

        for i in range(non_zero_ptr, len(nums)):
            nums[i] = 0


        