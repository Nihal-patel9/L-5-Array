def find_missing_numbers(nums1, nums2):
    distinct_nums1 = []
    distinct_nums2 = []

    for num in nums1:
        if num not in nums2 and num not in distinct_nums1:
            distinct_nums1.append(num)

    for num in nums2:
        if num not in nums1 and num not in distinct_nums2:
            distinct_nums2.append(num)

    return [distinct_nums1, distinct_nums2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
answer = find_missing_numbers(nums1, nums2)
print(answer)  # Output: [[1, 3], [4, 6]]
