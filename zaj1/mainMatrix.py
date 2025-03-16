import matrix

matrix1 = matrix.Matrix(1, 2, 3, 4)
matrix2 = matrix.Matrix(2, 0, 1, 2)
matrix3 = matrix1 + matrix2
print(matrix3)
print(repr(matrix3))
matrix4 = matrix1 * matrix2
print(matrix4)
print(repr(matrix4))