import os
import shutil

pathImages = "./message/"
pathDestino = "./images/"

archivos = os.listdir(pathImages)

# print archivos

for nombre in archivos:
    # print nombre[3:]
    desde = pathImages + nombre
    hasta = pathDestino + nombre[3:]
    shutil.copy(desde,hasta)

# for separador in archivos:
#     print (separador.split("-"))
