def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Sorted array for testing
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]

# Target value to search for
target_value = 7

# Perform binary search
result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in array.")
