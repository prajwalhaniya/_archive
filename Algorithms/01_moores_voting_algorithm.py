
def majortiy_element_using_mva(arr):
    n = len(arr)
    count = 0
    element = None

    for i in range(n):
        if count == 0:
            count += 1
            element = arr[i]
        elif element == arr[i]:
            count += 1
        else:
            count -= 1

    count_verification = 0
    for i in range(n):
        if arr[i] == element:
            count_verification += 1

    if count_verification > (n / 2):
        return element
    return -1

arr = [2, 2, 1, 1, 1, 2, 2]
print("MVA", majortiy_element_using_mva(arr))
