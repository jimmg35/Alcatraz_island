

# Author : @jimmg35
# using python typing module for static check
# python 3.7.3

from typing import List

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


input_str: str = "Hey dudes, how's going?"

row: int = 0
col:int = len(input_str.split(' '))
for i in input_str.split(' '):
    if len(i) > row:
        row = len(i)


total: List[List[str]] = []
for i in input_str.split(' '):
    temp: List[str] = []
    for j in range(0, row):
        try:
            temp.append(i[j])
        except:
            temp.append(" ")
    total.append(temp)

print(Transpose(total))



# [['H', 'd', 'h', 'g'], 
#  ['e', 'u', 'o', 'o'], 
#  ['y', 'd', 'w', 'i'], 
#  [' ', 'e', "'", 'n'], 
#  [' ', 's', 's', 'g'], 
#  [' ', ',', ' ', '?']]