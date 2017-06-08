#coding: utf-8

SIMBOLOS_TRANSFORMADOS = "qazwsxedcrfvtgbyhnujmikolp" + "ñ".decode('utf-8') + "=!\"#$%&/()|*+"

SIMBOLOS_ORIGINALES = "abcdefghijklmn" + 'ñ'.decode('utf-8') + "opqrstuvwxyz0123456789 .?"
    
# Función que realiza el proceso de encriptación

def encriptacion (mensaje):

    mensaje_encriptado = ""
    
    for caracter in mensaje:

        i = SIMBOLOS_ORIGINALES.find(caracter)

        mensaje_encriptado += SIMBOLOS_TRANSFORMADOS[i]
            
    print mensaje_encriptado

    i = 0

    primeros_caracteres = ""

    ultimos_caracteres = ""

    for caracter in mensaje_encriptado:

        if i < 3:

            primeros_caracteres += caracter

        else:

            ultimos_caracteres += caracter

        i += 1

    mensaje_encriptado = ultimos_caracteres + primeros_caracteres

    return mensaje_encriptado

# Función que realiza el proceso de decriptación

def desencriptar (mensaje):

    ultimos_caracteres = ""

    primeros_caracteres = ""

    mensaje_encriptado = ""

    i = 0
    
    for caracter in mensaje:

        if i <= len(mensaje) - 4:

            ultimos_caracteres += caracter

        else:

            primeros_caracteres += caracter

        i += 1

    mensaje = primeros_caracteres + ultimos_caracteres

    print mensaje

    for caracter in mensaje:

        i = SIMBOLOS_TRANSFORMADOS.find(caracter)

        mensaje_encriptado += SIMBOLOS_ORIGINALES[i]
        
    return mensaje_encriptado

# Función que pregunta por el mensaje al usuario, lo valida y lo procesa

def procesamiento(opcion):
    
    print " "
    
    #entrada
    
    mensaje = raw_input ("Ingrese el mensaje: ")
    
    mensaje = mensaje.decode('utf-8')
    
    mensaje = mensaje.lower()
    
    #validación
    
    if not mensaje.isdigit() and not mensaje.isalpha() and not mensaje.isalnum() and mensaje.find(' ') == -1 and mensaje.find('.') == -1 and mensaje.find('?') == -1 and mensaje.find('|') == -1 and mensaje.find('*') == -1 and mensaje.find('+') == -1:
        
        print "caracteres ingresados no válidos, inténtelo nuevamente"
        
        return procesamiento(opcion)
     
    elif opcion == '1':
        
        #Procesamiento y salida
        
        print "El mensaje encriptado es: " + encriptacion(mensaje)
        
        return 0
    
    elif opcion == '2':
        
        #Procesamientpo y salida
        
        print "El mensaje descriptado es: " + desencriptar(mensaje)
        
        return 0

# Función que presenta al programa y pregunta por cual operación realizar

def principal():
    
    print "Bienvenido a encriptador wikitiki"
    
    print " "

    print "Para utilizar el programa debe escojer alguna de estas opciones: "
    
    print " "
    
    print "(1) encriptar    (2) desencriptar"
    
    print " "
    
    # entrada
    
    eleccion = raw_input ("Ingrese un opcion: ")
    
    # Validación
    
    if eleccion != '1' and eleccion != '2' or not eleccion.isdigit():
        
        print "La opcion ingresada no es válida, inténtelo nuevamente"
        
        print " "
        
        return principal()
    
    # Se continua con el programa
    
    else:
        
        return procesamiento(eleccion)

# Se arranca el programa

if __name__ == '__main__':
    principal()