MENSAJE_DE_BIENVENIDA = '''
############################################

            SISTEMA DE PELICULAS

############################################
'''

MAIN_MENU_OPTIONS = [ " Ver peliculas", " Agregar peliculas", " Salir"]
VER_PELICULAS = [ " Pelicula 1", " Pelicula 2", " Pelicula 3"]

def saludar():
    print(MENSAJE_DE_BIENVENIDA)

def mostrar_menu_en_pantalla(opciones):
    index = 1
    for opcion in opciones:
        print (str(index) + opcion + " >")
        index = index +1

def validar_opcion(indice_opcion, opciones):
    return indice_opcion <= len(opciones) and indice_opcion > 0

def mostrar_menu(opciones, funcion):
    mostrar_menu_en_pantalla(opciones)
    inidice_opcion = obtener_input_usuarios()
    es_valido = validar_opcion(indice_opcion, opciones)
    if es_valido:
        funcionEsValida(indice_opcion)
    else:
        mostrar_menu(opciones, funcionvalida)

def funcionEsVAlida (opcion_elegida):
    if (opcion_elegida == 1):
        print ("Elegiste Opcion :", opcion_elegida)
    elif (opcion_elegida == 3):
        exit()

def valores (opcion_elegida):
    if (opcion_elegida == 1):
        mostrar_menu(VER_PELICULAS, verPelicula)
    elif (opcion_elegida == 2):
        print ("Agregar Pelicula")
    elif (opcion_elegida == 3):
        exit()

def obtener_input_usuarios():
    # print(chr(27)+"[1;33m"+"Ingrese opcion deseada : ")
    indice_opcion = int(raw_input(chr(27)+"[1;33m"+"Ingrese opcion deseada : "))
    print(chr(27)+"[0m")
    return indice_opcion

if __name__ == '__main__':
    saludar()
    mostrar_menu(MAIN_MENU_OPTIONS, funcion)
    obtener_input_usuarios()
