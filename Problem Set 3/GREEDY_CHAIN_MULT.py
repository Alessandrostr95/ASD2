import numpy as np

def GREEDY_CHAIN_MULT(A):
    
    if len(A) == 2:
        return A[0]*A[1]

    k = min( list( map( lambda k: (A[k].shape[0]*A[k].shape[1]*A[k+1].shape[1],k), list(range(len(A)-1)) ) ),  key=lambda tup: tup[0])[1]

    P = A[k]*A[k+1]
    A[k] = P
    A.pop(k+1)

    return GREEDY_CHAIN_MULT(A)