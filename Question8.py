def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []

    count = {}
    for num in changed:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    original = []
    for num in changed:
        if num not in count or count[num] == 0:
            continue

        count[num] -= 1

        if 2 * num not in count or count[2 * num] == 0:
            return []

        count[2 * num] -= 1
        original.append(num)

    return original


changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)  # Output: [1, 3, 4]
