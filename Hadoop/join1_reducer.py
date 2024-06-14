#!/usr/bin/env python
import sys

programa_actual = None
cuenta_actual = 0
es_abc = False

for entrada in sys.stdin:
    entrada = entrada.strip()
    nombre, dato = entrada.split('\t')

    if nombre != programa_actual:
        if programa_actual is not None and es_abc:
            print(f"{programa_actual} {cuenta_actual}")
        programa_actual = nombre
        cuenta_actual = 0
        es_abc = False

    if dato == 'ABC':
        es_abc = True
    else:
        cuenta_actual += int(dato)

# No olvides emitir el último programa si era de ABC
if es_abc:
    print(f"{programa_actual} {cuenta_actual}")
