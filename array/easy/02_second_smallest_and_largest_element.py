'''
- Find the largest and smallest element in a single traversal
- Find the second largest and second smallest by making use of the largest and smallest
'''

def get_second_smallest_and_largest_element(arr):
    n = len(arr)
    if n == 0 and n == 1:
        return -1

    small = float('inf')
    large = float('-inf')

    second_small = float('inf')
    second_large = float('-inf')

    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])

    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]

    return { second_small, second_large }

if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    print(get_second_smallest_and_largest_element(arr))
