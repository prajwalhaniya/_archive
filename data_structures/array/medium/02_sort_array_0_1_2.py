'''
- Keep count as there are only 0, 1 and 2 and then rewrite arr
- This problem is similar to dutch national flag algorithm
low, mid and high
'''

def sort_0_1_2(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [0, 2, 1, 2, 0, 1]
sort_0_1_2(arr)
print("After sorting:", arr)
