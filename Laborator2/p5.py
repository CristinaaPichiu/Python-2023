"""
    Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all
    the elements under the main diagonal with 0 (zero).
"""

def replace_below_main_diagonal_with_zeros(matrix):
    # funcția len(matrix) returnează lungimea listei matrix, care în acest caz este numărul de rânduri ale matricei.
    #Deoarece o matrice este o listă de liste, matrix[0] reprezintă prima listă din matrice, iar len(matrix[0]) returnează lungimea acestei liste, care reprezintă numărul de coloane
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Iterate through the matrix and replace elements below the main diagonal with 0
    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

if __name__ == "__main__":

 matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]

result = replace_below_main_diagonal_with_zeros(matrix)
for row in result:
    print(row)
