MENSAJE_DE_BIENVENIDA = '''
############################################

            SISTEMA DE PELICULAS

############################################
'''

MAIN_MENU_OPTIONS = ["ver peliculas","agregar peliculas"]

def saludar():
    print(MENSAJE_DE_BIENVENIDA)

def mostrar_menu_pantalla(opciones):
    index = 1
    for opcion in opciones:
        print (srt(index) + opcion + ">")
        index = index +1

def validar_opcion(indice_opcion, opciones):
    return indice_opcion <= len(opciones) and indice_opcion > 0

def mostrar_menu(opciones, funcEsValido):
    mostrar_menu_en_pantalla(opciones)



def obtener_input_usuarios():
    indice_opcion = int(raw_input("Ingrese opcion deseada"))
    return indice_opcion

if __name__ == '__main__'
    saludar()
    mostrar_menu_pantalla(MAIN_MENU_OPTIONS)
    obtener_input_usuarios()
