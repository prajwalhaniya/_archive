def quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    sample_array = [10, 7, 8, 9, 1, 5]
    sorted_array = quick_sort(sample_array)
    print("Sorted array:", sorted_array)
