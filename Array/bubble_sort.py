
def bubble_sort(arr):
    for i in range(len(arr) - 1):  # Outer loop to control the number of passes
        for j in range(len(arr) - 1 - i):  # Inner loop should reduce with each pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if the element is greater than the next element
    return arr

# Example usage:
unsorted_array = [10, 3, 6, 2, 7, 1, 5]
sorted_array = bubble_sort(unsorted_array)
print(sorted_array)  # Output: [1, 2, 3, 5, 6, 7, 10]

