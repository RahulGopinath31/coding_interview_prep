# Strassen’s Matrix Multiplication (Exploration)
# 1. Given two square matrices of size A and B of size n * n, find their matrix multiplication.
# [Hint: Try to solve the given problem using the Divide and Conquer Approach]
import numpy as np

def splitMat(Mat):
    row, col = Mat.shape
    row2, col2 = row//2, col//2

    return Mat[:row2, :col2], Mat[row2:, :col2], Mat[:row2, col2:], Mat[row2:, col2:]


def strassenMatMul(MatA, MatB):

    if len(MatA) == 1:
        return MatA * MatB
    
    a, b, c, d = splitMat(MatA)
    e, f, g, h = splitMat(MatB)

    p1 = strassenMatMul(a, f - h)
    p2 = strassenMatMul(a + b, h)
    p3 = strassenMatMul(c + d, e)
    p4 = strassenMatMul(d, g - e)
    p5 = strassenMatMul(a + d, e + h)
    p6 = strassenMatMul(b - d, g + h)
    p7 = strassenMatMul(a - c, e + f)

    # compute the values of the four quadrant
    q00 = p5 + p4 - p2 + p6
    q01 = p1 + p2
    q10 = p3 + p4
    q11 = p1 + p5 - p3 - p7

    MatProduct = np.vstack((np.hstack((q00, q01)),np.hstack((q10, q11))))

    return MatProduct


# Driver code
A = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]])
B = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [2, 2, 2, 2]])
print('Matrix multiplication result: ')
print(strassenMatMul(A, B))