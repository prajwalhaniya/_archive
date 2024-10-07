'''
- Using set
- Using two pointer approach
'''
from typing import List

def remove_duplicates(arr: List[int]):
    unique_numbers = set()
    for i in range(len(arr)):
        unique_numbers.add(arr[i])

    k = len(unique_numbers)
    j = 0

    for x in unique_numbers:
        arr[j] = x
        j += 1

    return k

# Using 2 pointer
def remove_duplicates_using_2_pointers(arr: List[int]):
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
        return arr
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3, 4, 5, 6]
    k = remove_duplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
    print()

    arr_after_removing_duplicates = remove_duplicates_using_2_pointers(arr)
    print("array after removing the duplicates", arr_after_removing_duplicates)
