import socket

HOST = '0.0.0.0'
PORT = 65000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # Escucho los puertos
s.listen(2) # se queda esperando a que se conecten 2 usuarios

user1, ip1 = s.accept() # acepta el primer cliente y le asigna una tupla
user2, ip2 = s.accept() # acepta el segundo cliente y le asigna una tupla

s.sendall("Todos los clientes conectados")

# while True:
#     msj = raw_input("escribe un mensaje: ")
#     s.sendto(msj ,(HOST, PORT))
#     recibido = s.recv(1024)
#     print("Recibido: ", recibido)
