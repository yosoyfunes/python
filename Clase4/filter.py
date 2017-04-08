loquebusco = raw_input("Ingrese un nombre:  ")

# para usar filter necesito crear una funcion que devuelva True o False
def buscar (l):
	return loquebusco in l

	# if loquebusco in l:
	# 	return True
	# else:
	# 	return False

nombres = ["Matias", "Javier", "Carolina", "Marcos"]
# filter (funcion, lista)

res = filter (buscar, nombres)
if (len(res) > 0):
	print(res)
else:
	print("no se encontraron resultados..")

# lista = filter (buscar, nombres)
# print (lista)
