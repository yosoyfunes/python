#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

HOST = '192.168.2.123' # Servidor
PORT = 65000           # Puerto del Servidor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creo mi objeto socket
s.bind(('0.0.0.0', 65001))  # Tiene la tupla "address", poner 0.0.0.0 quiere decir "para todas las interfaces de red estoy escuchando".


def recibe(socket):
    while True:
        mensaje, address = socket.recvfrom(1024)
        print("Recibido: ", mensaje)


def envia(socket):  # A quien, por donde, que.
    # password = str(raw_input("escribe la contraseña: "))
    password = "pindonga"
    socket.sendto(password, (HOST, PORT))
    while True:
        mensaje = raw_input("escribe un mensaje: ")
        if mensaje == "salir":
            exit()
        socket.sendto(mensaje, (HOST, PORT))

if __name__ == '__main__':
    thread_recibe = threading.Thread(target=recibe, args=(s,))
    thread_recibe.setDaemon(False)  # Espera indefinidamente a que termine esa tarea (es como poner un Join abajo)
    thread_recibe.start()  # Empieza a correr el Thread

    thread_enviar = threading.Thread(target=envia, args=(s,))
    thread_enviar.setDaemon(False)  # Espera indefinidamente a que termine esa tarea (es como poner un Join abajo)
    thread_enviar.start()  # Empieza a correr el Thread


