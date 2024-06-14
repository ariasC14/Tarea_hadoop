#!/usr/bin/env python
import sys

for entrada in sys.stdin:
    entrada = entrada.strip()  # Elimina cualquier espacio en blanco
    elementos = entrada.split(",")  # Divide la línea en elementos

    if len(elementos) != 2:
        continue  # Omite cualquier línea que no tenga exactamente dos elementos

    nombre, dato = elementos

    # Verifica si la parte 'dato' es un canal o un número de espectadores
    if dato.isdigit():
        # Es un recuento de espectadores, emite nombre y recuento de espectadores
        print(f"{nombre}\t{dato}")
    elif dato == 'ABC':
        # Es un programa de ABC, emite nombre y marcador de canal
        print(f"{nombre}\tABC")
