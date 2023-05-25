#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

datos2 = []
for line in sys.stdin:
    key, value1, value2 = line.strip().split('\t')
    datos2.append((key,value1,int(value2)))
datos2.sort(key=lambda x: (x[0], x[2], x[1]))


for item in datos2:
      clave, valor1, valor2 = item
      print(f"{clave}   {valor1}   {valor2}")