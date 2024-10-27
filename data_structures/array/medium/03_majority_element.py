from collections import Counter

def majority_element(arr):
    n = len(arr)
    counter = Counter(arr)

    for num, count in counter.items():
        if count > (n // 2):
            return num
    return -1

# Optimal approach - Moore's voting algorithm
'''
- Keep track of occurrences of majority and minory element dynamically
'''

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
ans = majority_element(arr)
print("The majority element is:", ans)
print("MVA", majortiy_element_using_mva(arr))
