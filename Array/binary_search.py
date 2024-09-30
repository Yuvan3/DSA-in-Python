def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2 # Find the middle index

        if arr[middle] == target:
            return middle # Target found, return index
        elif arr[middle] < target:
            left = middle + 1  # Search in the right half
        else:
            right = middle - 1  # Search in the left half

    return -1  # Target not found

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")