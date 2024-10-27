'''
Approaches:
1: Sort and return
2: Use second_small and second_largest variable (use two loops)
    - Find the largest and smallest element in a single traversal
    - Find the second largest and second smallest by making use of the largest and smallest
3: Best approach
    No two loops, use only one loop

    - If the current element is smaller than ‘small’, then we update second_small and small variables
    - Else if the current element is smaller than ‘second_small’ then we update the variable ‘second_small’
    - Once we traverse the entire array, we would find the second smallest element in the variable second_small.
    similary for second_largest
'''

# Approach 2
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

# Approach 3
def second_smallest(arr):
    if (len(arr) < 2):
        return -1

    small = float('inf')
    second_small = float('inf')

    for i in range(len(arr)):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]

    return second_small

def second_large(arr):
    if (len(arr) < 2):
        return -1

    large = float('-inf')
    second_large = float('-inf')

    for i in range(len(arr)):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]

    return second_large



if __name__ == '__main__':
    arr = [1, 2, 4, 6, 7, 5]
    n = len(arr)
    print(get_second_smallest_and_largest_element(arr))
    print(second_smallest(arr))
    print(second_large(arr))
