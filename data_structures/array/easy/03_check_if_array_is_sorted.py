def check_if_array_is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 5
    print("True" if check_if_array_is_sorted(arr) else "False")
