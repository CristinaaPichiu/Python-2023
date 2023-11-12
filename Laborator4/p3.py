class Matrix:

    # Constructor
    def __init__(self, n, m):
        # Initialize the matrix with dimensions n x m, filled with zeros
        self.rows = n
        self.cols = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        """Get the element at position (i, j)"""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.matrix[i][j]
        return None

    def set(self, i, j, value):
        """Set the element at position (i, j) to the given value"""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.matrix[i][j] = value

    def transpose(self):
        transposed = []
        for j in range(self.cols):
            transposed_row = []
            for i in range(self.rows):
                transposed_row.append(self.matrix[i][j])
            transposed.append(transposed_row)

        self.matrix = transposed
        self.rows, self.cols = self.cols, self.rows
        
    def matrix_multiplication(self, other):
        """Matrix multiplication with another Matrix object"""
        if self.cols != other.rows:
            return None  # Matrices cannot be multiplied

        # Multiply matrices and return the result in a new matrix
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]

        return result

    def apply_transformation(self, function):
        """Apply a transformation (lambda function) to each element of the matrix"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = function(self.matrix[i][j])


# Example usage
if __name__ == "__main__":
    matrix1 = Matrix(3, 3)
    values = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Initialize matrix1 with predefined values
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            matrix1.set(i, j, values[i][j])

    print("Original Matrix:")
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            print(matrix1.get(i, j), end=' ')
        print()

    matrix1.apply_transformation(lambda x: x * 2)  # Apply a transformation (multiplying by 2)

    print("Transformed Matrix:")
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            print(matrix1.get(i, j), end=' ')
        print()

    matrix2 = Matrix(3, 2)
    values_matrix2 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    # Initialize matrix2 with predefined values
    for i in range(matrix2.rows):
        for j in range(matrix2.cols):
            matrix2.set(i, j, values_matrix2[i][j])

    product = matrix1.matrix_multiplication(matrix2)
    if product:
        print("Result of Matrix Multiplication:")
        for i in range(product.rows):
            for j in range(product.cols):
                print(product.get(i, j), end=' ')
            print()

    matrix1.transpose()  # Transpose the matrix1

    print("Transposed Matrix:")
    for i in range(matrix1.rows):
        for j in range(matrix1.cols):
            print(matrix1.get(i, j), end=' ')
        print()
