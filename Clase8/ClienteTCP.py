import socket

HOST = '192.168.2.123'
PORT = 65000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

recibido = s.recv(1024)
print("Recibido: ", recibido)
