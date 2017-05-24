# Echo cliente programa
import socket

def abrirConexion():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def cerrarConexion():
    s.close()

def enviarMensaje(mensaje):
    # s.sendto("Mensaje" ,(HOST, PORT))
    HOST = '192.168.2.68' # Servidor de Lucas
    PORT = 80             # Puerto del server
    s.sendto(mensaje ,(HOST, PORT))

if __name__ == '__main__':
    abrirConexion()

    while True:
        msj = raw_input("escribe un mensaje:")
        enviarMensaje(msj)

    cerrarConexion()
