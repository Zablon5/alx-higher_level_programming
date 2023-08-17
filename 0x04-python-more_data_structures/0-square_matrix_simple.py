#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    a function that returns
    the squre of a givrn matrix
    """
    return (list(map(lambda row:(list(map(lambda col:col*col,row))),matrix)))
    