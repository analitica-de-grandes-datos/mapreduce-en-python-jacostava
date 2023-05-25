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
    key, value = line.strip().split(',')
    letras.append(key)
    numeros.append(int(value))
    datos = list(zip(letras,numeros))
#print(f"{datos}")

lista2 = []
for clave, grupo in itertools.groupby(datos,lambda x:x[0]):
    listanums = []
    for cont in grupo:
        listanums.append(cont[1])
    trio = (clave,sorted(listanums))
    lista2.append(trio)

for item in lista2:
     nums = ",".join(str(valor) for valor in (item[1]))
     print(f"{item[0]}\t{str(nums)}")