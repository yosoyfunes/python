import hashlib

handshakes = open("handshakes.lst", "r")
diccionario = open("Spanish.dic", "r")

# contenidoHandshake = handshakes.read()
# contenidoDiccionario = diccionario.read()

# imprime el contenido

# for dic in diccionario.readlines():
for dic in contenidoDiccionario:
    archivoConvertioenHash = hashlib.sha1(dic).hexdigest()
    if "63494b1130f6979ea6b61980b6fa03049502078b" == archivoConvertioenHash:
        print "el nombre es: " + dic

    # print "Nombre:"+dic+" Hash:"+archivoConvertioenHash
