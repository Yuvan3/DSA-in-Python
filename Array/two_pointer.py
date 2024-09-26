
def two_sum(numbers, target):
    left = 0
    right = len(numbers)-1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left, right] 
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Example usage:
numbers = [2, 7, 11, 15]
target = 22
result = two_sum(numbers, target)
print(result)