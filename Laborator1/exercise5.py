def spiral_matrix_to_string(matrix):
    if not matrix:
        return ""

    result = ""
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result += matrix[top][i]
        top += 1

        for i in range(top, bottom + 1):
            result += matrix[i][right]
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result += matrix[bottom][i]
            bottom -= 1

        if left <= right:
            # Traverse leftmost column
            for i in range(bottom, top - 1, -1):
                result += matrix[i][left]
            left += 1

    return result

matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiral_matrix_to_string(matrix)
print(result)