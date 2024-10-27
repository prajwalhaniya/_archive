from re import L


def max_subarray_sum(arr):
    max_sum = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            arr_sum = 0
            for k in range(i, j + 1):
                arr_sum += arr[k]
            max_sum = max(max_sum, arr_sum)

    return max_sum

# better approach
def max_subarray_better_approach(arr):
    max_sum = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            max_sum = max(max_sum, sum)
    return max_sum

# Kadane's algorithm
def kadanes_algorithm(arr):
    max = 0
    sum = 0

    for i in range(n):
        sum += arr[i]

        if sum > max:
            max = sum

        if sum < 0:
            sum = 0

    return max

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 3, 1, -5, 4]
    n = len(arr)
    max_sum = max_subarray_sum(arr)
    print("The maximum subarray sum is:", max_sum)
    max_sum_2 = max_subarray_better_approach(arr)
    print("The maximum subarray sum is:", max_sum_2)
    max_sum_3 = kadanes_algorithm(arr)
    print("The maximum subarray sum is:", max_sum_3)
