from SatSolver import *

if __name__ == '__main__':
    Formula = SATInstance()
    Formula.importa("FORMULA_SAT.txt")
    print( Formula.formula() )
    print( Formula.solve() )
