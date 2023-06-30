def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1

    while left <= right:
        if abs(nums[left]) >= abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1

    return result


nums = [-4, -1, 0, 3, 10]
result = sorted_squares(nums)
print(result)  # Output: [0, 1, 9, 16, 100]
