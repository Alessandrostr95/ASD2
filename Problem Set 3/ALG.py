def ALG(a):

    a.append(0)
    a.sort()

    C = OPT(a)

    return ["START"] + procedura_ricorsiva(a, C, 0, len(a)-1)

def OPT(a):

    n = len(a)

    C = [ [float("inf")]*n for _ in range(n) ]

    for i in range(n):
        C[i][i] = 0

    for s in range(1,n):
        for i in range(n-s):
            j = i + s
            '''i < k <= j'''
            ks = list(range(i+1,j+1))

            '''OPT(i,j) = min{ (abs(a_i - a_k) - 200)^2 + OPT(k,j) }'''
            C[i][j] = min(list(map(lambda k:  (abs(a[i] - a[k]) - 200)**2 + C[k][j], ks))) 
    
    return C

def procedura_ricorsiva(a, C, i, j):

    if i == j:
        return ["STOP"]

    k = i+1
    while C[i][j] != C[i][k] + C[k][j]:
        k += 1
    
    return [a[k]] + procedura_ricorsiva(a, C, k, j)

print( ALG([0,0,0,0,150,300,450,600]) )
