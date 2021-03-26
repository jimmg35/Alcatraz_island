

# Author : @jimmg35
# using python typing module for static check
# python 3.7.3

from typing import List

def dotProduct(vector_1: List[float], vector_2: List[float]) -> float:
    sums: float = 0
    for i in range(0, len(vector_1)):
        sums += vector_1[i] * vector_2[i]
    return sums

def getShape(matrix: List[List[str]]) -> List[int]:
    # return row, col of a matrix
    return [len(matrix), len(matrix[0])]

def Transpose(A) -> List[List[str]]:
    # transpose a matrix
    shape_A: List[int] = getShape(A)
    if shape_A[0] != 1:
        result: List[List[str]] = []
        for i in range(0, shape_A[1]):
            v: List[str] = []
            for j in range(0, shape_A[0]):
                v.append(A[j][i])
            result.append(v)
        return result
    else: #if A is row matrix
        return [[A[i]] for i in range(0, len(A))]

matrix: List[List[float]] = [[0,1,-2],
                             [-1,0,3], 
                             [2,-3,0]]

matrix_T = Transpose(matrix)

final: float = 0
for i in range(0, len(matrix_T)):
    for j in range(i+1, len(matrix_T)):
        final += dotProduct(matrix_T[i], matrix_T[j])

if final == 0:
    print("This is a orthogonal matrix!")
else:
    print("This matrix is not orthogonal!")