import punto3
import random

def random_dimensions(n=1,i=3,j=4):
    l = []
    for _ in range(n):
        random.seed(random.randint(0,1000))
        l.append(i)
        l.append(j)
        i = j
        j = random.randint(2,20)
    return l


m = int(input("Quanti test eseguire? "))
n = int(input("Quanto devono essere lunghe le catene per i test? "))

print("\n\nGREEDY\t|\tDYNAMIC")

p = 0

for _ in range(m):
    (greedy, dynamic) = punto3.COUNT_MULT( random_dimensions( n ) )
    p += dynamic/greedy

print(p/m)
