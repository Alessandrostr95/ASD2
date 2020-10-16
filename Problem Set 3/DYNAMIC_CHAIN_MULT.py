import numpy as np

def OPT(A):

    n = len(A)
    C = [ [0]*n for _ in range(n) ]
    
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            C[i][j] = min( list(map(lambda k: A[i].shape[0] * A[k].shape[1] * A[j].shape[1] + C[i][k] + C[k+1][j], list(range(i,j)))) )

    return C

def CHAIN_MULT(A):

    global O
    O = OPT(A)

    return procedura_ricorsiva(A,0,len(A)-1)

def procedura_ricorsiva(A,i,j):

    if i == j:
        return A[i]
    
    k = i
    while O[i][j] != A[i].shape[0]*A[k].shape[1]*A[j].shape[1] + O[i][k] + O[k+1][j]:
        k += 1

    X = procedura_ricorsiva(A,i,k)
    Y = procedura_ricorsiva(A,k+1,j)
    
    return X*Y