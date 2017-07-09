python
======

> Archivos de python


**Ejemplos de Python Y entornos Virtuales**
=====================================

+ Instalar Python 2.7
+ Instalar Python 3.6


**Comando py en Windows**

Antes teniamos que hacer algo como esto 

```
C:\Python27\lib\python.exe --version
Python 2.7.11
C:\Python36\lib\python.exe --version
Python3.4
```

Ahora hacemos esto con Py Launcher en Windows 7/8/8.1/10

```
py -2   -m pip install SomePackage  # default Python 2
py -27  -m pip install SomePackage  # specifically Python 2.7
py -3   -m pip install SomePackage  # default Python 3
py -36  -m pip install SomePackage  # specifically Python 3.6
```
**Comando virtualenv**

```
py -2   -m pip install virtualenv  # default Python 2
py -27  -m pip install virtualenv  # specifically Python 2.7
py -3   -m pip install virtualenv  # default Python 3
py -36  -m pip install virtualenv  # specifically Python 3.6
```

**Creando Entornos virtuales**
```
py -2   -m virtualenv entornoNombre  # default Python 2
py -27  -m virtualenv entornoNombre2.7  # specifically Python 2.7
py -3   -m virtualenv entornoNombre3  # default Python 3
py -36  -m virtualenv entornoNombre3.4  # specifically Python 3.6
```


**Activando Entornos**
```
c:\env\entorno27\Scripts\activate
o
c:\env\entorno36\Scripts\activate

```

**Desactivandolos**

Se escribe "deactivate" en cualquier parte que estemos si esta habiliado un entorno lo cerrara

```
deactivate

```

**Comprobando Versiones**

La ventaja es que ya no necesitamos sobreponer python -m, ya que esta implicito que es la de la version del python que pusismos pero supongamos es una maquina y nos dicen instala los paquetes en la maquina virtual, y queremos saber que version de python y de pip hacemos lo siguiente:

```
python --version
Python 2.7.11
python -m pip --version
pip 8.1.1 from C:\env\entorno2.7\lib\site-packages (python 2.7)
```
** Verificando Paquetes instalados**

```
python -m pip list
	Django (1.9.2)
	pip (8.1.1)
	setuptools (21.0.0)
	wheel (0.29.0)
```

**Creando Archivo de requeriments.txt**

```
python -m pip freeze > requeriments.txt

```
**Instalando desde requeriments.txt**


```
python -m pip install -r requeriments.txt

```

