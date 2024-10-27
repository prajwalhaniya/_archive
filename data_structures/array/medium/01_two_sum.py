'''
Given: target, arr
return index of elements if the target sum can be achieved with the arr elements

Brute force: 2 loops if (arr[i] + arr[j]) == target
Optimised approach: Use dict, complement
'''

def two_sum(arr, target):
    num_map = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = [2, 8, 3, 7]
target = 9
result = two_sum(nums, target)
print("Indices of the two numbers that add up to the target:", result)
