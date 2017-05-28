#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time

# Creo una clase Contador que extiende de la clase thread y redefino la funcion run()

class Contador(threading.Thread):
    def __init__(self, numero):
        threading.Thread.__init__(self) # redefino el contructor
        self.numero = numero

    def run(self):
        while (self.numero > 0):
            print ("Numero: ", self.numero)
            time.sleep(2) # genero un retaardo de 2 segundos
            self.numero = self.numero - 1

if __name__ == '__main__':
    thread = Contador(10)
    thread.start()
    thread.join()


# def Mifuncion(argumento1, argumento2):
#     print 'En thread'
#     print 'Los Argumentos pasados son: ', argumento1, argumento2
#
#
# if __name__ == '__main__':
#     Variable1 = "Variable Uno"
#     Variable2 = "Variable Dos"
#
#     thread = Thread(target=Mifuncion, args=(Variable1, Variable2))
#     thread.start()