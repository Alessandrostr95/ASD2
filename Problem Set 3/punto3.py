from copy import deepcopy

'''
a deve essere una lista di interi positivi. Verranno eseguiti dei controlli per verificare se a
rappresenta effettivamente le dimensioni di una sequenza ordinata di matrici
'''
def COUNT_MULT(a):

    if len(a)%2 != 0:
        raise Exception("Il numero di elementi nella sequnza deve essere necessariamente pari")
    
    dim = []
    for i in range(0,len(a),2):
        dim.append((a[i],a[i+1]))
    
    
    for i in range(len(dim)-1):
        if dim[i][1] != dim[i+1][0]:
            raise Exception("Dimensioni incoerenti")

    greedy = GREEDY_COST(deepcopy(dim))
    dynamic = DYNAMIC_COST(deepcopy(dim))
    
    #print("GREEDY : " + str(greedy))
    #print("DYNAMIC : " + str(dynamic))

    return (greedy, dynamic)


def GREEDY_COST(a):

    if len(a) == 2:
        return a[0][0]*a[0][1]*a[1][1]

    k = min( list( map( lambda k: (a[k][0]*a[k][1]*a[k+1][1],k), list(range(len(a)-1)) ) ),  key=lambda tup: tup[0])[1]

    ret = a[k][0]*a[k][1]*a[k+1][1]

    a[k] = (a[k][0],a[k+1][1])
    a.pop(k+1)

    return ret + GREEDY_COST(a)


def DYNAMIC_COST(a):
    
    n = len(a)
    C = [ [0]*n for _ in range(n) ]
    
    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            C[i][j] = min( list(map(lambda k: a[i][0] * a[k][1] * a[j][1] + C[i][k] + C[k+1][j], list(range(i,j)))) )

    return C[0][len(a)-1]
