# http://www.taringa.net/posts/hazlo-tu-mismo/17698845/Compilar-tu-programa-en-Python-en-un-exe-unico.html

from distutils.core import setup 
import py2exe 
import os 

setup(console=["md5.py"]) 