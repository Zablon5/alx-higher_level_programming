def square_matrix_simple(matrix=[]):
    n = len(matrix)
    m = len(matrix[0])
    new_matrix = []
    for i in range(n):
        current=[]
        for j in matrix[i]:
            current.append(j*j)
        new_matrix.append(current)   
    return new_matrix     