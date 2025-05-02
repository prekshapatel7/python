'''Write a program that implements a Matrix class and performs addition,
multiplication and transpose operations on 3x3 matrices.'''
class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Matrix must be 3x3")
        self.data = data

    def display(self):
        for row in self.data:
            print(row)

    def add(self, other):
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        result = [
            [self.data[j][i] for j in range(3)]
            for i in range(3)
        ]
        return Matrix(result)

# Example matrices
matrix1 = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

matrix2 = Matrix([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

# Perform operations
print("Matrix 1:")
matrix1.display()

print("\nMatrix 2:")
matrix2.display()

print("\nAddition:")
matrix1.add(matrix2).display()

print("\nMultiplication:")
matrix1.multiply(matrix2).display()

print("\nTranspose of Matrix 1:")
matrix1.transpose().display()
