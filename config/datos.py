#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib
import os
import ConfigParser
	
try:
	f = open('config.ini', 'r')
except IOError:
	print "error abriendo archivo de configuracion"
else:
	f.close()
	config = ConfigParser.RawConfigParser()
	config.read('config.ini')

	# Datos FTP
	ftp_servidor = config.get('FTP', 'servidor')
	ftp_usuario  = config.get('FTP', 'user')
	ftp_clave    = config.get('FTP', 'password').decode('base64')
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
			print "archivo %s subido exitosamente" % fichero_destino
		except:
			print "No se ha podido encontrar el fichero " + fichero_origen
	except:
		print "No se ha podido conectar al servidor " + ftp_servidor
