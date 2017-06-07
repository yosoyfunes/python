#!/usr/bin/env python
# -*- coding: cp1252 -*-

import ftplib
import os

# Datos FTP
ftp_servidor = 'ftp.servidor.com'
ftp_usuario  = 'miusuario'
ftp_clave    = 'miclave'
ftp_raiz     = '/public_html' # Carpeta del servidor donde queremos subir el fichero
 
# Datos del fichero a subir
fichero_origen = '/home/usuario/mifichero.zip' # Ruta al fichero que vamos a subir
fichero_destino = 'mifichero.zip' # Nombre que tendrá el fichero en el servidor

# Conectamos con el servidor
try:
	s = ftplib.FTP(ftp_servidor, ftp_usuario, ftp_clave)
	print "conectado al servidor " + ftp_servidor
	try:
		f = open(fichero_origen, 'rb')
		s.cwd(ftp_raiz)
		s.storbinary('STOR ' + fichero_destino, f)
		f.close()
		s.quit()
		print "archivo " + fichero_destino + " subido exitosamente"
	except:
		print "No se ha podido encontrar el fichero " + fichero_origen
except:
	print "No se ha podido conectar al servidor " + ftp_servidor
