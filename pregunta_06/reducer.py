#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import itertools
from operator import itemgetter

letras = []
numeros = []
datos = []
for line in sys.stdin:
    key, value = line.strip().split('\t')
    letras.append(key)
    numeros.append(float(value))
    datos = list(zip(letras,numeros))

lista2 = []
for clave, grupo in itertools.groupby(datos,lambda x:x[0]):
    listanums = []
    for cont in grupo:
        listanums.append(cont[1])
    trio = (clave,max(listanums),min(listanums))
    lista2.append(trio)

for item in lista2:
    clave, maximo, minimo = item
    print(f"{clave}\t{maximo}\t{minimo}")