def find_obstructed_seats(matrix):
    obstructed_seats = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for row in range(num_rows):
        for col in range(num_cols):
            current_height = matrix[row][col]
            obstructed = False

            for i in range(row + 1, num_rows):
                if matrix[i][col] > current_height:
                    obstructed = True
                    break

            if obstructed:
                obstructed_seats.append((row, col))

    return obstructed_seats

if __name__ == "__main":
    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    obstructed_seats = find_obstructed_seats(stadium)
    print(obstructed_seats)
