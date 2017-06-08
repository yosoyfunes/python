# http://www.taringa.net/posts/hazlo-tu-mismo/17698845/Compilar-tu-programa-en-Python-en-un-exe-unico.html
# https://geekytheory.com/generar-un-ejecutable-exe-a-partir-de-un-py/

from distutils.core import setup 
import py2exe 
import os 

#setup(console=["md5.py"]) 

setup(name="PyToFox", 
 version="1.0", 
 description="Libreria PyToFox", 
 author="Matias Anoniz", 
 author_email="desarrollo@memosoft.com.ar", 
 url="www.memosoft.com.ar", 
 license="(C) Copyright  memosoft.com.ar", 
 Copyright="(C) Copyright  memosoft.com.ar",
 scripts=["md5.py"], 
 console=["md5.py"], 
 options={"py2exe": {"bundle_files": 1}}, 
 zipfile=None,
)