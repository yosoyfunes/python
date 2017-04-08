loquebusco = raw_input("Ingrese un nombre:  ")

# para usar filter necesito crear una funcion que devuelva True o False
def funcion_buscar (l):
	return loquebusco in l

	# if loquebusco in l:
	# 	return True
	# else:
	# 	return False

lista_nombres = ["Matias", "Javier", "Carolina", "Marcos"]
# filter (funcion, lista)

datos = filter (funcion_buscar, lista_nombres)
if (len(datos) > 0):
	print(datos)
else:
	print("no se encontraron resultados..")

# lista = filter (buscar, nombres)
# print (lista)
