def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

numbers = [1, 2, 4, 6, 7, 8, 10]
target_number = 6
result = binary_search(numbers, target_number)

if result != -1:
    print(f"Element {target_number} found at index {result}.")
else:
    print(f"Element {target_number} not found in the list.")
