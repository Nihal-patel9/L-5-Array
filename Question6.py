def findDuplicates(nums):
    duplicates = []

    for i in range(len(nums)):

        num = abs(nums[i])

        if nums[num - 1] > 0:

            nums[num - 1] *= -1
        else:
            duplicates.append(num)

    return duplicates


nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result)  # Output: [2, 3]
