#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser

ftp_servidor = 'ftp.servidor.com'
ftp_usuario  = 'miusuario'
ftp_clave    = 'miclave'

config = ConfigParser.RawConfigParser()

config.add_section('FTP')
config.set('FTP', 'username', ftp_usuario)
config.set('FTP', 'password', ftp_clave.encode('base64'))
config.set('FTP', 'servidor', ftp_servidor)

# Creo un archivo config.ini
with open('config.ini', 'wb') as configfile:
    config.write(configfile)
