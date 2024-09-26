import random

def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a random pivot
    pivot = random.choice(arr)

    # Partition the array into elements less than, equal to, and greater than the pivot
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Recursively sort the less and greater parts, then combine them with the equal part
    return quick_sort(less) + equal + quick_sort(greater)
    

# Example usage:
unsorted_array = [10, 3, 6, 2, 7, 1, 5]
sorted_array = quick_sort(unsorted_array)
print(sorted_array) # Output: [1, 2, 3, 5, 6, 7, 10]