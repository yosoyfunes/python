#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import hashlib library (md5 method is part of it)
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
        #print "File: ", file_name
        try:
            # Open,close, read file and calculate MD5 on its contents
            with open(file_name, 'rb') as file_to_check:
                block_size = 65536
                mhash = hashlib.md5()
                while True:
                        data = file_to_check.read(block_size)
                        if not data:
                            break
                        else:
                            mhash.update(data)
                            md5_returned = mhash.hexdigest()

            #print "HASH MD5: ", md5_returned
            destino = file_name[:len(file_name)-4]+'_'+md5_returned+file_name[-4:]
            shutil.copy(file_name, destino.upper())
        except IOError, e:
            print "no se puede abrir el archivo"
            #print e
    else:
        data = sys.argv[1]
        print "Dato: ", data
        md5_returned = hashlib.md5(data).hexdigest()
        print "HASH MD5: ", md5_returned
