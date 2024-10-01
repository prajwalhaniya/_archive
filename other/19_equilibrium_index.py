def equilibrium_index(arr: list[int]) -> int:
    total_sum = sum(arr)
    left_sum = 0

    for i, value in enumerate(arr):
        total_sum -= value
        if left_sum == total_sum:
            return i
        left_sum += value
    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print(equilibrium_index(arr))