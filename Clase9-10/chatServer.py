#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creo mi objeto socket
s.bind(('0.0.0.0', 65000))  # Tiene la tupla "adress", poner 0.0.0.0 quiere decir "para todas las interfaces de red estoy escuchando".
print("Empiezo a escuchar")


def recibe(socket):
    mensaje_inicial = 'pindonga'  # contrasenia para entrar
    todas_las_address = set()
    while True:
        elmensajeposta = ""
        mensaje, address = socket.recvfrom(1024)
        if mensaje == mensaje_inicial:
            todas_las_address.add(address)
            elmensajeposta = "<" + str(address) + " Se conecto >"
        else:
            elmensajeposta = mensaje

        for conn in todas_las_address:
            thread_envio = threading.Thread(target=envia, args=(conn, socket, elmensajeposta))
            print(conn)
            thread_envio.start()


def envia(address, socket, mensaje):  # A quien, por donde, que.
    socket.sendto(mensaje, (address[0], 65001))


if __name__ == '__main__':
    thread_recibe = threading.Thread(target=recibe, args=(s,))
    thread_recibe.setDaemon(False)  # Espera indefinidamente a que termine esa tarea (es como poner un Join abajo)
    thread_recibe.start()  # Empieza a correr el Thread

# thread_envia = threading.Thread(target = envia , args=(address, s , mensaje ))