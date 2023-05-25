#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(" ")
    campo1 = str(lista[3][5:7])
    print(f"{campo1}")