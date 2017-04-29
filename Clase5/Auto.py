# Clase Auto
# debe comenzar con Mayuscula y siempre lleva como parametro self

class Auto:
    def __init__(self, color="Blanco"):
        self.color = color

    def dameColor(self):
        return self.color

a = Auto()
b = Auto("Rojo")
print ("El auto a tiene color: %s") % (a.dameColor())
print ("El auto a tiene color: %s") % (b.dameColor())
