'''
- Sort and return the last element [ O(n*logn)]
- Using a max variable [O(n)]
'''

from typing import List

def find_largest_element(arr: List):
    max = arr[0]
    n = len(arr)
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]

    return max

if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    max = find_largest_element(arr1)
    print("The largest element in the array is:", max)
