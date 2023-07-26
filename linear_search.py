def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


numbers = [2, 7, 1, 10, 6, 8, 4]
target_number = 6
result = linear_search(numbers, target_number)

if result != -1:
    print(f"Element {target_number} found at index {result}.")
else:
    print(f"Element {target_number} not found in the list.")
