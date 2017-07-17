#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

includefiles = ['layout/', 'img/', 'src/']
includes = []
excludes = ['Tkinter']
packages = ['os','PyQt5', 'sqlalchemy']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

company_name = 'Trabajo Practico'
product_name = 'PyPET'

shortcut_table = [
    ("DesktopShortcut",         
     "DesktopFolder",           
     "Tool",                    
     "TARGETDIR",               
     "[TARGETDIR]\main.exe",    
     "TARGETDIR",               
     )
    ]

target = Executable(
    script="main.py",
    base= base,
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
        options = {
                'build_exe': {'includes':includes, 'excludes':excludes, 'packages':packages, 'include_files':includefiles, "include_msvcr": True},
                'build_msi': msi_options
        }, 
        executables=[target]
     )