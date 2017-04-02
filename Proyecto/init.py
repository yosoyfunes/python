MENSAJE_DE_BIENVENIDA = '''
###############################################################

                      SISTEMA DE PELICULAS

###############################################################
'''

MAIN_MENU_OPTIONS = [" Ver peliculas", " Agregar peliculas", " Salir"]
VER_PELICULAS = [" Pelicula 1", " Pelicula 2", " Pelicula 3"]


def saludar():
    print (MENSAJE_DE_BIENVENIDA)

def cls():
	print (chr(27)+"[0m")

def mostrar_menu_en_pantalla(opciones):
    index = 1
    for opcion in opciones:
        print (str(index) + opcion + " >")
        index = index +1

def validar_opcion(opcion_elegida, opciones_en_lista):
    # Devuelve cantidad de opciones que hay en la lista de MAIN_MENU_OPTIONS
    return opcion_elegida <= len(opciones_en_lista) and opcion_elegida > 0

def mostrar_menu(opciones, funciones):
    mostrar_menu_en_pantalla(opciones)
    numero_de_opcion = obtener_input_usuarios()
    es_valido = validar_opcion(numero_de_opcion, opciones)
    if es_valido:
        funcionEsValida(numero_de_opcion)
    else:
        print("Opcion Incorrecta, ingrese una opcion")
        mostrar_menu(opciones, numero_de_opcion)

def funcionEsValida (opcion_elegida):
    if (opcion_elegida == 1):
        print ("Elegiste en esta opcion, y elegiste :", opcion_elegida)
    elif (opcion_elegida == 2):
        print ("Elegiste la Opcion :", opcion_elegida)
    elif (opcion_elegida == 3):
        exit()

def obtener_input_usuarios():
    # print(chr(27)+"[1;33m"+"Ingrese opcion deseada : ")
    indice_opcion = int(raw_input(chr(27)+"[1;36m"+"Ingrese opcion deseada : "+chr(27)+"[0m"))
    return indice_opcion

if __name__ == '__main__':
    saludar()
    mostrar_menu(MAIN_MENU_OPTIONS, funcionEsValida)