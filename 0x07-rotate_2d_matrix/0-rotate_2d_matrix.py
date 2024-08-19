#!/usr/bin/python3
""" Rotate a 2d array """

def rotate_2d_matrix(matrix):
    """ rotate a 2d array """
    n = len(matrix)

    # Step 1: Transpose the matrix (convert rows to columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
