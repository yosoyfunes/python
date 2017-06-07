#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import hashlib library (incluye metodo > md5)
# Importo sys para pasar por argumento el nombre del archivo
# Importo shutil para manejo de archivos, copiar, renombrar, etc
import sys
import hashlib   
import os, shutil

# Argumento pasado por linea de comando //
# [0] es el nombre del PATH // [1] el el 1er argumento

if len(sys.argv) == 1:
    print """
    Generador de HASH MEMOSOFT
    Modo de uso: 
    
    md5.exe [ archivo ]
    
    (C) Copyright  memosoft.com.ar
    
    """
else:
    file_name = sys.argv[1]

    if os.path.isfile(file_name):
        try:
            archivo =  open(file_name, 'rb')
            data = archivo.read()
            hashmd5 = hashlib.md5(data).hexdigest()

            destino = file_name[:len(file_name)-4]+'_'+hashmd5+file_name[-4:]
            shutil.copy(file_name, destino.upper())
        except IOError, e:
            print "no se puede abrir el archivo"
            #print e
    else:
        data = sys.argv[1]
        print "Dato: ", data
        hashmd5 = hashlib.md5(data).hexdigest()
        print "HASH MD5: ", hashmd5
