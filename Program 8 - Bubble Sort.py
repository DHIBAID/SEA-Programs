def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


user_input = input("Enter numbers separated by space: ")
nums = list(map(int, user_input.split()))
bubble_sort(nums)
print("Sorted array:", nums)
