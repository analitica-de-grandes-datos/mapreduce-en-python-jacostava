#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

datos2 = []
for line in sys.stdin:
    key, value = line.strip().split('\t')
    campo1 = line[0].strip()
    campo2 = line[2].strip()
    datos2.append((campo1,campo2))    
datos2.sort(key=lambda x: (x[1], x[0]))

for item in datos2:
     clave, valor = item
     print(f"{clave},{valor}")