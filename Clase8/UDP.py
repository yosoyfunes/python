import socket

HOST = '192.168.2.68' # Servidor de Lucas
PORT = 65000          # Puerto del Servidor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.sendto("Mensaje" ,(HOST, PORT))


s.bind(("0.0.0.0", PORT))

while True:
    msj = raw_input("escribe un mensaje: ")
    s.sendto(msj ,(HOST, PORT))
    recibido = s.recv(1024)
    print("Recibido: ", recibido)
