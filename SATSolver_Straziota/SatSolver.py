class SATInstance:
    '''
        Costruttore di classe.
        Ogni variabile x è rappresentata con un numero intero k
        I letterali del tipo 'x' sono rappresentati col numero 2k
        mentre i letterali del tipo '~x' con 2k+1.
        Di conseguenza le calusole sono rappresentate con delle tuple di interi,
        dove ogni elemento rappresenta un letterale.

            Es:
                variabili = {x, y, z}
                valori associati alle variabili = {
                    x : 0,
                    y : 1,
                    z : 2
                }

            Una clausola del tipo '(~x OR y OR ~z)' sarà rappresentata con la tupla (1, 2, 5)
    '''
    def __init__(self):
        # Tabella che associa a una var un numero da 0 a n-1
        self.tavola_var = dict()
        # lista di clausole
        self.clausole = []
        self.pred = None
    
    '''
        Metodo che data una stringa, la trasforma in una clausola e la inserisce nella formula
    '''
    def parse(self, clausola):
        try:
            c = []
            for letterale in clausola.split():
                negata = (letterale[0] == '~')
                nome_var = letterale[1:] if negata else letterale[:]
                self.tavola_var.setdefault(nome_var, len(self.tavola_var) )
                c.append( self.tavola_var[nome_var] << 1 | negata )
            self.clausole.append( tuple(sorted(c)) )
        except:
            raise Exception("Parse error: Not valid input")
    

    '''
        Metodo che, dato un percorso file, legge la codifica di una espressione booleana
        e ne aggiunge le clausole all'oggetto chiamante.

        Un file di testo con 3 clausole deve essere della forma:
        X ~Y Z
        ~X ~Z
        W Y
    '''
    def importa(self, path):
        f = open(path, 'r')
        for riga in f:
            self.parse( riga.strip() )
        f.close()

    '''
        Metodo che dato un numero intero
        ritorna una stringa che rappresenta il letterale ad esso associato
        Es:
            1 --> ~x
    '''
    def literal_to_string(self, letterale):
        s = '~' if letterale & 1 else ''
        return s + list(self.tavola_var.keys())[letterale >> 1]
    
    '''
        Metodo che data una sequenza intera
        restituisce una stringa che rappresenta la clausola ad esso associata.
        Es:
            (1, 2, 5) --> ~x y ~z
    '''
    def clause_to_string(self, clausola):
        return ' '.join(self.literal_to_string(l) for l in clausola)
    
    '''
        Metodo che restituisce una stringa che
        rappresenta l'intera formula
    '''
    def formula(self):
        s = 'Formula: '
        for c in self.clausole:
            s += f"({self.clause_to_string(c)}), "
        return s[:-2]
    
    '''
        Metodo che data una assegnazione di verità
        ritorna una stringa che ne rappresenta l'assegnazione.

        Es:
            Variabili = {A, B, C}
            Assegnazione = [1, 1, 0]
            Return -> A B ~C
        
        Se brief=True allora verranno rappresentate solamente le variabili alle
        quali è stato assegnato il valore True

        Es:
            Variabili = {A, B, C}
            Assegnazione = [1, 1, 0]
            brief = True
            Return -> A B
    '''
    def assignment_to_string(self, assignment, brief=False):
        literals = []
        for a, v in ((a, v) for a, v in zip(assignment, self.tavola_var.keys())):
            if a == 0 and not brief:
                literals.append('~' + v)
            elif a:
                literals.append(v)
        return ' '.join(literals)


    '''
        Metodo che data una variabile 'x' è una assegnazione per tale variabile
        restituisce una nuova ISTANZA, dove sono rimosse tutte le clausole soddisfatte
        da tale assegnazione, oppure se la clausola iniziale non è stata soddisfatta
        allora semplicemente rimuove dove è presente la var 'x'.

        Esempio:
            Formula = (x OR y) AND (~x OR y)
            Formula.assing('x', 0)  -->  new Instance = (y)             # assegno 'False' alla variabile 'x'


    '''
    def assign(self, variabile, assignment):
        newInst = SATInstance()
        var = self.tavola_var[variabile]

        for clausola in self.clausole:

            if var << 1 in clausola and assignment == 0:
                '''
                    Nella clausola è presente "x" e gli sto assegnango False
                    perciò rimuovo semplicemente "x" dalla clausola
                '''
                newInst.parse( self.clause_to_string( tuple( i for i in clausola if i != var << 1 ) ) )

            elif var << 1 | 1 in clausola and assignment == 1:
                '''
                    Nella clausola è presente "~x", ma dato che ho assegnato True a "x"
                    allora "~x"= False. Non soddisfando la clausola, tolgo "~x".
                '''
                newInst.parse( self.clause_to_string( tuple( i for i in clausola if i != var << 1 | 1 ) ) )
            
            elif var << 1 not in clausola and var << 1 | 1 not in clausola:
                ''' La variabile "x" non è presente nella clausola, perciò la conservo integra'''
                newInst.parse( self.clause_to_string( clausola ) )

        return newInst
    
    def solve(self):
        S = [self]
        result = {}

        while len(S) > 0:
            # CHOOSE
            P = S.pop()

            # Scelgo una variabile a caso al suo interno
            x = list(P.tavola_var.keys())[0]

            # EXPAND & TEST
            for i in [0,1]:
            
                P_i = P.assign(x, i)
                P_i.pred = (P, x, i)

                if len(P_i.clausole) == 0:
                    return self.soluzione( P_i )
                elif () not in P_i.clausole:
                    S.append( P_i )

        return None
    

    '''
        Metodo, cha data un faoglia dell'albero di ricerca
        ritorna l'assegnzione di verità composta dagli archi
        che vanno da tale nodo alla radice
    '''
    @staticmethod
    def soluzione(p):
        assegnazione = {}
        edge = p.pred
        while edge != None:
            assegnazione[edge[1]] = edge[2]
            edge = edge[0].pred
        return assegnazione