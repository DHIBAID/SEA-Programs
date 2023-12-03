import random

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

array_size, min_val, max_val = 20, 1, 100
random_list = sorted([random.randint(min_val, max_val) for _ in range(array_size)])
target_value = random.randint(min_val, max_val)

result = binary_search(random_list, target_value)
print(f"Target value {target_value} found at index: {result}" if result != -1 else f"Target value {target_value} not found in the list.")
