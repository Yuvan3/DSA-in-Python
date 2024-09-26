# space_complexity_examples.py

# O(1) - Constant Space Example
def sum_of_elements(lst):
    """
    Calculates the sum of elements in the list.
    Space Complexity: O(1) - The amount of extra memory used is constant, regardless of the input size.
    """
    total = 0  # Only one variable is used regardless of list size
    for element in lst:
        total += element
    return total

# O(n) - Linear Space Example
def create_duplicate_list(lst):
    """
    Creates a duplicate of the input list.
    Space Complexity: O(n) - The amount of extra memory used grows linearly with the input size.
    """
    new_list = []  # A new list is created, which is proportional in size to the input list
    for element in lst:
        new_list.append(element)
    return new_list

# O(n^2) - Quadratic Space Example
def create_2d_array(n):
    """
    Creates a 2D array (matrix) of size n x n.
    Space Complexity: O(n^2) - The amount of extra memory used grows quadratically with the input size.
    """
    array = [[0] * n for _ in range(n)]  # A 2D array with n rows and n columns is created
    return array

# O(log n) - Logarithmic Space Example
def binary_search(arr, low, high, x):
    """
    Performs binary search using recursion.
    Space Complexity: O(log n) - The amount of extra memory used is proportional to the recursion depth, which is logarithmic.
    """
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Example Usage:
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]

    # O(1) example
    print("O(1) - Sum of elements:", sum_of_elements(sample_list))

    # O(n) example
    print("\nO(n) - Duplicate list:", create_duplicate_list(sample_list))

    # O(n^2) example
    n = 3
    print(f"\nO(n^2) - 2D Array of size {n}x{n}:")
    for row in create_2d_array(n):
        print(row)

    # O(log n) example
    sorted_list = [1, 3, 5, 7, 9, 11]
    element_to_find = 7
    print(f"\nO(log n) - Binary Search for {element_to_find}:")
    index = binary_search(sorted_list, 0, len(sorted_list) - 1, element_to_find)
    print(f"Element {element_to_find} found at index:", index)
