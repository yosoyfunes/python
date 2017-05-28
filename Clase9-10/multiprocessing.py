#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time

def contador(numero):
    while (numero > 0):
        print ("Numero: ", numero)
        time.sleep(2) # genero un retaardo de 2 segundos
        numero -= 1

if __name__ == '__main__':
    p = Process(target=contador, args=(20,))
    p.start()
    p.join()

