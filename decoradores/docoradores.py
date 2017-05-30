def agrega_enfasis(enfasis):
    def decorator(f):
        def funcion():
            value = f()
            if enfasis is True:
                value += "!!!"

            print(value)

        return funcion

    return decorator

@agrega_enfasis(True)
def wellcome():
    return "hello"

@agrega_enfasis(False)
def saludar():
    return "hola"

if __name__ == '__main__':
    wellcome()
    saludar()