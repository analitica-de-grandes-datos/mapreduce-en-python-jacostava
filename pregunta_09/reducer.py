#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter

datos2 = []
for line in sys.stdin:
    key, value1, value2 = line.strip().split('\t')
    datos2.append((key,value1,int(value2)))
datos2.sort(key=itemgetter(2))    

for item in datos2:
      clave, valor1, valor2 = item
      if valor2 <= 7:
        print(f"{clave}   {valor1}   {valor2}")