python
======

> Archivos de python


**Ejemplos de Python y entornos Virtuales en WINDOWS**
=========================================

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


**VirtualEnvs (entornos virtuales python) en LINUX**
-------------------------------------------

Crear y gestionar VirtualEnvs (entornos virtuales) en Python.

Un problema común que se puede encontrar un desarrollador de python es el de coexistencias de versiones.

Por ejemplo:

 - Estamos desarrollando varios programas en python simultáneamente, uno en Python 2.x y otro con Python 3.
 - Estamos desarrollando varios programas que utilizan versiones diferentes de una misma librerías externa (de las que importamos al inicio de nuestro programa).
 - Necesitamos desarrollar un programa que utiliza versiones de librerías externas que no coinciden con las que vienen por defecto en nuestra distribución.
 - Hemos desarrollado un programa que utiliza una versión concreta de una librería externa, y un upgrade de versión en nuestra distribución actualiza esa librería y deja de funcionar el programa (suponiendo que la nueva versión no tenga compatibilidad total descendente).
 - Queremos desarrollar o ejecutar programas Python en un entorno en el cual no tenemos acceso root y por tanto no podemos instalar paquetes de librerías python que necesitamos.

Para solucionar esto, en Python se pueden crear "entornos virtuales", que son directorios dentro de los cuales podemos instalar librerías de Python (tanto "últimas versiones" como "versiones concretas (más antiguas)" de las mismas), y que no interfieren con los que tenemos instalados en nuestra distribución Linux. De hecho, ningún programa Python los utilizará a menos que ejecutemos el programa dentro del entorno virtual (momento en que el "import XYZ" cargará la librería XYZ del entorno virtual, y no la del sistema).

Aunque se denomina "entorno virtual", lo que vamos a ver no tiene nada que ver con el concepto de virtualización. El nombre oficial es "virtualenv" pero, más bien, es algo parecido a un "chroot" de Linux.

Pues bien, el concepto de trabajo es el siguiente:


Creamos un entorno virtual (que no es más que un directorio de trabajo) para unas condiciones concretas de nuestra aplicación (por ejemplo, una versión concreta de una librería).
Entramos en el entorno virtual (nos cambiamos de nuestra "shell de trabajo" a una "shell dentro del entorno virtual".
Estando dentro del entorno virtual, instalamos con pip las librerías deseadas. La instalación no será en el sistema sino dentro del entorno virtual (en un directorio site-packages dentro del directorio de trabajo del entorno).
Podemos ubicar los fuentes de nuestra aplicación donde deseemos, no tiene por qué estar dentro del entorno virtual. Si la ejecutamos en una shell "normal" (fuera del virtualenv) se utilizarán los paquetes del sistema. Si la ejecutamos estando dentro de la "shell del entorno virtual", los "import XYZ" cargarán las librerías instaladas dentro del entorno virtual. Es decir, podemos tener los fuentes donde queramos pero debemos ejecutarlo dentro del entorno virtual.
Cuando queramos, podemos salir del entorno virtual para volver al "entorno estándar".

Vamos a verlo con un ejemplo que incluye:


 - Instalación del software para crear entornos virtuales.
 - Creación de un entorno virtual.
 - Entrada en un entorno virtual.
 - Instalación de librerías dentro del entorno virtual.
 - Ejecución de un programa en el entorno virtual.
 - Salida del entorno virtual.


**Instalar virtualenv**
-----------------------------

Para poder utilizar entornos virtuales en Python, basta con instalar los paquetes adecuados:

**Distribuciones basadas en RPM / YUM:**

    yum install python-virtualenv

**Distribuciones basadas en DEB / APT:**

    apt-get install python-virtualenv

También es posible instalar virtualenv usando "pip", el "instalador de librerías" de Python (el equivalente Python del CPAN de perl). No obstante, la instalación mediante "pip" no será un "paquete RPM/DEB" del sistema sino descarga directa de la biblioteca e instalación en el directorio "/usr/local/lib/python/site-packages" del sistema.

**Instalar virtualenv usando "pip"** 

    apt-get install python-pip

    pip install virtualenv

**Creación de un entorno virtual**

Con el paquete de virtualenv ya creado, vamos a proceder a crear entornos virtuales.

Para ello, lo normal es crear un directorio base de trabajo donde crear tantos entornos virtuales como deseemos:

    cd $HOME
    mkdir pythonenvs
    cd pythonenvs

**Después, creamos el entorno virtual:**


    virtualenv proyecto

Virtualenv creará un directorio "proyecto". Dentro de este directorio, veremos que virtualenv ha creado unos subdirectorios "bin", "include" y "etc", como si fuera el árbol de directorios de un sistema Linux (como ya comenté, es parecido a un chroot).

Dentro del directorio lib/ de nuestro entorno virtual, se habrá creado un subdirectorio "site-packages" que es donde se instalarán los paquetes si usamos "pip install" dentro del entorno virtual.

Dentro del directorio bin/ tendremos una copia del intérprete de python (del binario). Si no hemos indicado ningún flag, copiará el intérprete por defecto, pero podemos crear un virtualenv específico para probar nuestra aplicación con una versión de python (que tengamos instalada) concreta:

    virtualenv --python=/usr/bin/python2.7 proyecto

Podemos crear tantos entornos virtuales como queramos. Por ejemplo, podemos tener uno con una versión de una librería, y otro con otra, con el objetivo de testear el mismo programa en python con las diferentes versiones (ejecutando el mismo programa dentro de un entorno virtual, o del otro).

Finalmente, a la hora de crear virtualenvs, hay un flag de interés que debemos conocer: **–system-site-packages:**

Si creamos el entorno virtual, y entramos dentro de ese entorno, los programas python que ejecutemos dentro del entorno sólo tendrán "conocimiento" de las bibliotecas estándar de python y de las bibliotecas instaladas dentro del entorno virtual (en su lib/site-packages). Un programa python no podrá hacer uso (import) de bibliotecas instaladas "en el sistema" (fuera del virtualenv) vía gestor de paquetes o vía pip. Es decir, que aunque tengamos una biblioteca instalada en el sistema, dentro del entorno virtual no será visible, es decir, el intérprete de python del entorno virtual no verá lo que haya instalado en el site-packages del sistema.

Esto es así por defecto al crear un virtualenv para tener un control absoluto de las versiones y bibliotecas que tenemos dentro del mismo, pero podemos cambiar este comportamiento con el flag –system-site-packages:

    virtualenv --system-site-packages proyecto

Usando este flag, los programas python ejecutados dentro del virtualenv verán tanto las librerías instaladas en el mismo como las librerías instaladas en el sistema.


Entrada en un entorno virtual

    cd proyecto
    source bin/activate

Veremos que el prompt de la shell cambia a:

    (proyecto)$ _

Instalación de librerías dentro del entorno virtual

Dentro de un entorno virtual, podemos usar "pip" para instalar bibliotecas no estándar de python (en lib/site-packages). Si no instalamos librerías dentro de nuestro entorno virtual, sólo tendremos disponibles los módulos de la librería estándar de python (os, sys, etc…).

    (proyecto)$ pip install feedparser

Feedparser se descargará e instalará, pero en lib/site-packages en el directorio local del virtualenv.

Podemos incluso instalar versiones específicas de librerías, y usar pip con sus flags habituales (pero sólo verá los paquetes instalados dentro del entorno virtual):

    (proyecto)$ pip install 'ZopeSkel==2.21.2'

Al igual que fuera de los virtualenvs, también podremos usar freeze, upgrade, search y uninstall:

    (proyecto)$ pip freeze
    (proyecto)$ pip install --upgrade ZopeSkel
    (proyecto)$ pip search cadena_a_buscar
    (proyecto)$ pip uninstall paquete

Ejecución de un programa en el entorno virtual.

Con el prompt dentro del entorno virtual, la ejecución de nuestro programa se realizará de forma que se utilizará el intérprete de Python que se instaló dentro del virtualenv al crearlo, y nuestro programa sólo podrá importar las bibliotecas instaladas en el virtualenv (a menos que hayamos utilizado al crearlo la opción –system-site-packages.

Podemos estar alojar el programa en python en cualquier lugar del filesystem y editarlo dentro o fuera del virtualenv. Lo importante es ejecutarlo en la shell del virtualenv para que se utilice el entorno definido.


**Salida del un entorno virtual**

Para salir del entorno virtual, se utiliza el comando "deactivate":

    (proyecto)$ deactivate

Al ejecutarlo, volveremos a la "shell normal". Ejecutar un programa python en esta shell normal utilizará las librerías python del sistema, y el programa no tendrá ningún tipo de visibilidad (ni cargará) las versiones que teníamos instaladas en el site-packages del entorno virtual.


**virtualenvwrapper: haciendo más sencillos los venvs**
-------------------------------------------------------

Si instalamos el paquete "virtualenvwrapper", dispondremos de una serie de "atajos" para hacer más sencillo el uso de los virtualenvs:

    pip install virtualenvwrapper

Después, en nuestro **~/.bashrc** ponemos:

    export WORKON_HOME=~/pythonenvs/
    source /usr/local/bin/virtualenvwrapper.sh

Tras esto, podemos crear, entrar y salir de entornos virtuales con:

**Crear un nuevo entorno virtual**

    mkvirtualenv proyecto2

**Cambiarnos a un entorno virtual**

    workon proyecto2


**Salir del entorno virtual**

    deactivate


**Listar todos los entornos virtuales existentes en WORKON_HOME**

    lsvirtualenv


**Eliminar (ojo: borrar) un entorno virtual cuando ya no lo necesitemos**

    rmvirtualenv proyecto2


