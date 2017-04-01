MENSAJE_DE_BIENVENIDA = '''
############################################

            SISTEMA DE PELICULAS

############################################
'''

MAIN_MENU_OPTIONS = [" Ver peliculas"," Agregar peliculas"]

def saludar():
    print(MENSAJE_DE_BIENVENIDA)

def mostrar_menu_en_pantalla(opciones):
    index = 1
    for opcion in opciones:
        print (str(index) + opcion + " >")
        index = index +1

def validar_opcion(indice_opcion, opciones):
    return indice_opcion <= len(opciones) and indice_opcion > 0

def mostrar_menu(opciones, funcEsValido):
    mostrar_menu_en_pantalla(opciones)
    inidice_opcion = obtener_input_usuarios()
    es_valido = validar_opcion(indice_opcion, opciones)
    if es_valido:
        funcionEsValida(indice_opcion)
    else:
        mostrar_menu(opciones, funcionvalida)

def funcionEsVAlida (opcion_elegida)
    if (opcion_elegida == 1):
        print ("Elegiste Opcion :", opcion_elegida)

def obtener_input_usuarios():
    # print(chr(27)+"[1;33m"+"Ingrese opcion deseada : ")
    indice_opcion = int(raw_input(chr(27)+"[1;33m"+"Ingrese opcion deseada : "))
    print(chr(27)+"[0m")
    return indice_opcion

if __name__ == '__main__':
    saludar()
    mostrar_menu(MAIN_MENU_OPTIONS, 1)
    obtener_input_usuarios()
