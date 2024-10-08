# Kadane's algorithm
def kadanes_algorithm(arr):
    n = len(arr)
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
    max_sum_3 = kadanes_algorithm(arr)
    print("The maximum subarray sum is:", max_sum_3)
