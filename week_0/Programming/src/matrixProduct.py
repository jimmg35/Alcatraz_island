

# A = [[1,2,3],    
#      [4,5,6],     
#      [7,8,9]]    
# B = [[1,2], 
#      [3,4],
#      [5,6]]


# A = [[1],
#      [2],
#      [3]]
# B = [1,2,3,4]


# A = [1,2,3]
# B = [[1,2], 
#      [3,4],
#      [5,6]]


def getShape(A):
    try:
        return (len(A), len(A[0]))
    except:  #if this matrix is row matrix
        return (1, len(A))
          
def Transpose(A):
    
    shape_A = getShape(A)
    if shape_A[0] != 1:
        result = []
        for i in range(0, shape_A[1]):
            v = []
            for j in range(0, shape_A[0]):
                v.append(A[j][i])
            result.append(v)
        return result
    else: #if A is row matrix
        return [[A[i]] for i in range(0, len(A))]

def InnerProduct(v, w):
    norm = 0
    for i in range(0, len(v)):
        norm += v[i] * w[i]
    return norm

def MatrixProduct(A, B):
    
    shape_A = getShape(A)
    shape_B = getShape(B)
    B_T = Transpose(B)
    
    if shape_A[1] == shape_B[0]:
        # initialize the output matrix
        result = [[0 for j in range(0, shape_B[1])] for i in range(0, shape_A[0])]
        # start calculation
        for i in range(0, shape_A[0]):
            for j in range(0, shape_B[1]):
                try:
                    result[i][j] = InnerProduct(A[i], B_T[j])
                except:
                    result[i][j] = InnerProduct(A, B_T[j])
        
        return result
    else:
        return "none"
    
    
    
print(MatrixProduct(A, B))