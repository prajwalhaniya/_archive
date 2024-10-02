def recursive_insertion_sort(arr, n):
    if n <= 1:
        return

    recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last


arr = [5, 2, 9, 7, 14, 8]
n = len(arr)
recursive_insertion_sort(arr, n)
print("Sorted array:", arr)
