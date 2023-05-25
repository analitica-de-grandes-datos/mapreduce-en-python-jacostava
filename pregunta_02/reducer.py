#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
validador = 0
for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key == current_key:
        if int(value) > validador:
            validador = max(validador,int(value))
    else:
        if current_key is not None:
            print(f"{current_key}\t{validador}")
        current_key = key
        validador = int(value)     

# Imprimir el último resultado parcial
if current_key is not None:
     print(f"{current_key}\t{validador}")