#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

def contador(numero, hilo):
    while (numero > 0):
        print(numero, hilo)
        numero = numero - 1

if __name__ == '__main__':
    t1 = threading.Thread(target=contador, args=(200,"T1"))
    t2 = threading.Thread(target=contador, args=(100,"T2"))

    # Tengo que pasarle el nombre de la funcion con terget=
    # porque si la paso con variable la ejecuto.
#	t3 = threading.Thread(contador(50, "T3"))
#	t3.start()

    t1.start()  #  threads.append(t1)
    t2.start()


# https://www.genbetadev.com/python/multiprocesamiento-en-python-threads-a-fondo-introduccion