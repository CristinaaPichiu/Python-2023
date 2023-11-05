class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrix[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrix[i][j] = value

    def transpose(self):
        transposed = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                transposed[j][i] = self.matrix[i][j]
        self.n, self.m = self.m, self.n
        self.matrix = transposed

    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Matrix dimensions are not compatible for multiplication.")
        result = Matrix(self.n, other.m)
        for i in range(result.n):
            for j in range(result.m):
                result.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.m))
        return result

    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = func(self.matrix[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])


# Example usage:
if __name__ == "__main__":
    # Create a 3x2 matrix
    matrix_a = Matrix(3, 2)
    matrix_a.set(0, 0, 1)
    matrix_a.set(0, 1, 2)
    matrix_a.set(1, 0, 3)
    matrix_a.set(1, 1, 4)
    matrix_a.set(2, 0, 5)
    matrix_a.set(2, 1, 6)

    print("Matrix A:")
    print(matrix_a)

    # Transpose the matrix
    matrix_a.transpose()
    print("\nTransposed Matrix A:")
    print(matrix_a)

    # Create a 3x2 matrix
    matrix_b = Matrix(3, 2)
    matrix_b.set(0, 0, 7)
    matrix_b.set(0, 1, 8)
    matrix_b.set(1, 0, 9)
    matrix_b.set(1, 1, 10)
    matrix_b.set(2, 0, 11)
    matrix_b.set(2, 1, 12)

    print("\nMatrix B:")
    print(matrix_b)

    # Multiply Matrix A and Matrix B
    result = matrix_a.multiply(matrix_b)
    print("\nMatrix A * Matrix B:")
    print(result)


