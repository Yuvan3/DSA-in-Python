# Merge Sort

"""
Explanation:
Base Case: The merge_sort function recursively splits the array until it reaches the base case where the array has only one element or is empty.
Splitting: The array is split into two halves using the middle index.
Merging: The merge function takes two sorted arrays and merges them into a single sorted array by comparing elements from both arrays.
Complexity: The time complexity of Merge Sort is O(n log n), which is efficient for large datasets. The space complexity is O(n) due to the auxiliary arrays used in merging.
"""

def merge_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle of the array
    mid = len(arr) // 2
    
    # Recursively split and sort both halves
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge the two arrays by comparing their elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # If there are remaining elements in the left or right half, add them to the result
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
unsorted_array = [10, 3, 6, 2, 7, 1, 5]
sorted_array = merge_sort(unsorted_array)
print(sorted_array)  # Output: [1, 2, 3, 5, 6, 7, 10]



