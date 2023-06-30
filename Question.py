def convert_to_2d_array(original, m, n):
    if len(original) != m * n:
        return []

    result = [[0] * n for _ in range(m)]
    row, col = 0, 0

    for num in original:
        result[row][col] = num
        col += 1
        if col == n:
            col = 0
            row += 1

    return result


original = [1, 2, 3, 4]
m = 2
n = 2

result = convert_to_2d_array(original, m, n)
print(result)  # Output: [[1, 2], [3, 4]]
