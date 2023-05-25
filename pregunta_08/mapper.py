#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(" ")
    campo1 = lista[0]
    campo2 = int(lista[6])
    print(f"{campo1}\t{campo2}")