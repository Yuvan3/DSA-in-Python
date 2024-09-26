# time_complexity_examples.py

# O(1) - Constant Time Example
def get_first_element(lst):
    """
    Returns the first element of the list.
    Time Complexity: O(1) - The operation takes constant time regardless of the list size.
    """
    return lst[0]

# O(n) - Linear Time Example
def print_elements(lst):
    """
    Prints each element of the list.
    Time Complexity: O(n) - The operation takes time proportional to the number of elements in the list.
    """
    for element in lst:
        print(element)

# O(n^2) - Quadratic Time Example
def print_pairs(lst):
    """
    Prints all pairs of elements in the list.
    Time Complexity: O(n^2) - The operation takes time proportional to the square of the number of elements.
    """
    for i in lst:
        for j in lst:
            print(i, j)

# O(log n) - Logarithmic Time Example
def binary_search(arr, x):
    """
    Performs binary search on a sorted array to find the element 'x'.
    Time Complexity: O(log n) - The operation takes logarithmic time with respect to the number of elements.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# O(2^n) - Exponential Time Example
def fibonacci(n):
    """
    Recursively calculates the nth Fibonacci number.
    Time Complexity: O(2^n) - The operation takes exponential time as it repeatedly solves overlapping subproblems.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example Usage:
if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]

    # O(1) example
    print("O(1) - Get first element:", get_first_element(sample_list))

    # O(n) example
    print("\nO(n) - Print elements:")
    print_elements(sample_list)

    # O(n^2) example
    print("\nO(n^2) - Print pairs:")
    print_pairs(sample_list)

    # O(log n) example
    sorted_list = [1, 3, 5, 7, 9, 11]
    element_to_find = 7
    print("\nO(log n) - Binary Search:")
    print(f"Element {element_to_find} found at index:", binary_search(sorted_list, element_to_find))

    # O(2^n) example
    print("\nO(2^n) - Fibonacci:")
    print("Fibonacci of 5:", fibonacci(5))
