
# Minimum Size Subarray Sum

def min_subarray_len(target, nums):
    left = 0
    min_len = 1000000000
    current_sum = 0
    left = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != 1000000000 else 0


nums = [2,3,1,2,4,3]
target = 7

print(min_subarray_len(target, nums))