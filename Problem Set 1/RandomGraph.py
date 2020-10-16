from random import random

def prob(p):
    return (random() <= p)

def test(n, p, numeroditest):
    casifavorevoli = 0
    for i in range(numeroditest):
        G = Graph()
        G.createRandom(n,p)
        if G.isConnected():
            casifavorevoli += 1
    return casifavorevoli/numeroditest

class Node:
    def __init__(self, contenuto=None):
        self.contenuto = contenuto
        self.vicini = []

    @staticmethod
    def vicini(a, b):
        return (b in a.vicini) or (a in b.vicini)

    def __str__(self):
        s = '[{}]\t-->'.format(str(self.contenuto))
        for v in self.vicini:
            s += '({}), '.format(str(v.contenuto))
        return s


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add(self, nodes):
        for n in nodes:
            self.nodes.append(Node(n))
        
    def attach(self, i, j, w=0):
        self.nodes[i].vicini.append(self.nodes[j])
        self.nodes[j].vicini.append(self.nodes[i])
        '''
        Questa informazione è superflua e ridondante ai fini del software,
        l'ho inserita nel caso possa essere ustile in scopi futuri
        '''
        self.edges.append({
            "nodeA": self.nodes[i],
            "nodeB": self.nodes[j],
            "w": w
        })

    def createRandom(self, n, p):
        self.add( list( range(n) ) )
        
        
        for i in range(len(self.nodes)-1):
            for j in range(i+1,len(self.nodes)):
                if not Node.vicini(self.nodes[i], self.nodes[j]) and prob(p):
                    self.attach(i,j)


    def DFS(self):
        for v in self.nodes:
            v.visitato = False
        
        self.nodes[0].visitato = True
        pila = [self.nodes[0]]

        ret = []

        while len(pila) != 0:
            u = pila.pop()

            ret.append(u)

            for v in u.vicini:
                if not v.visitato:
                    v.visitato = True
                    pila.append(v)
        
        return ret
    
    def isConnected(self):
        return len(self.DFS()) == len(self.nodes)
        




    def __str__(self):
        s = ''
        for v in self.nodes:
            s += str(v) + '\n'
        return s
        


print('\t\t\t############# RANDOM G_n,p #############')
print('\n\nQuesto programma genera casualmente dei grafi G_n,p ed effettua dei test per verificare con che percentuale (in base a p) i grafi sono connessi.')
print("IMPORTANTE: E' possibile decidere quanti grafi creare per test, pero' dato che il programma e' pensato SOLAMENTE per sperimentare (e non per essere particolarmente efficiente) e' consigliato di non superare le 10000 unita' per test.\n\n")
numeroditest = int(input('Numero di grafi creati per test ?'))

''' TEST 1'''
n = 100
p = 0.05
print('\n\n\tTEST 1\t')
print('n = {}\np = {}'.format(n,p))
print("p e' circa log(n)/n")
print("G e' connesso con una probabilita del " + str(test(n, p, numeroditest)*100) + "%" )

''' TEST 2'''
n = 100
p = 0.1
print('\n\n\tTEST 2\t')
print('n = {}\np = {}'.format(n,p))
print('p > log(n)/n')
print("G e' connesso con una probabilita del " + str(test(n, p, numeroditest)*100) + "%" )

''' TEST 3'''
n = 100
p = 0.01
print('\n\n\tTEST 3\t')
print('n = {}\np = {}'.format(n,p))
print('p < log(n)/n')
print( "G e' connesso con una probabilita del " + str(test(n, p, numeroditest)*100) + "%" )





