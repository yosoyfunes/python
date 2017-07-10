#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# python -m compileall .

includefiles = ['layout/', 'img/', 'clientes.py', 'base.py', 'buscarClientes.py']
includes = []
excludes = ['Tkinter']
packages = ['os','PyQt5', 'sqlalchemy']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

company_name = 'Trabajo Practico'
product_name = 'PyPET'

bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': True,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    # 'includes': ['atexit', 'PySide.QtNetwork'], # <-- this causes error
    }

shortcut_table = [
    ("DesktopShortcut",         # Shortcut
     "DesktopFolder",           # Directory_
     "Tool",                    # Name
     "TARGETDIR",               # Component_
     "[TARGETDIR]\main.exe",    # Target
     None,                      # Arguments
     None,                      # Description
     None,                      # Hotkey
     None,                      # Icon
     None,                      # IconIndex
     None,                      # ShowCmd
     "TARGETDIR",               # WkDir
     )
    ]

target = Executable(
    script="main.py",
    base= base,
#    compress=False,
#    copyDependentFiles=True,
#    appendScriptToExe=True,
#    appendScriptToLibrary=False,
    icon='img/farmacia.ico',
    shortcutName="Sistema de Turnos",
    shortcutDir="DesktopFolder",
    )

msi_data = {"Shortcut": shortcut_table}

msi_options = {
    'includes':includes,
    'add_to_path': True, 
    'excludes':excludes,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name), 
    'packages':packages, 
    'include_files':includefiles, 
    "include_msvcr": True,
    "data": msi_data}

setup(  name = "PyPet",
        version = "1.0.1",
        description = "Sistema de Veterinaria" ,
        author="Matias Anoniz",
        # options = {"build_exe": build_exe_options},
        options = {
                'build_exe': {'includes':includes, 'excludes':excludes, 'packages':packages, 'include_files':includefiles, "include_msvcr": True},
                'build_msi': msi_options
        }, 
        # executables = [Executable("main.pyw", base=base)])
        executables=[target]
     )

'''  1. Este archivo le he llamado ejecutable.py. Llámale como quieras
     2. Sustituye en Executable el nombre del archivo py o pyw  por el que quieres convertir a exe.
     3. Abre la línea de comandos en Windows, sitúate en el directorio donde tengas el archivo ejecutable.py y el archivo a convertir en exe y escribe
    la siguiente línea de comando:

    py ejecutable.py build

    4.Esto te creará una carpeta build que contiene el ejecutable y todos los archivos necesarios
    NOTA: Recuerda que debes tener instalado cx_freeze. 
    Lo puedes hacer desde la línea de comandos con:  pip install cx_Freeze

'''

'''
target = Executable(
    script="your_program.py",
    base="Win32GUI",
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="icon.ico"
    )

setup(
    name="name",
    version="1.0",
    description="the description",
    author="the author",
    options={"build_exe": options},
    executables=[target]
    )

'''