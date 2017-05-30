class bad_cat():
    def __init__(self):
        self.nya = 'Pepe Argento'

    def art_deco(func): 
        """funcion decorador"""
        def handle_error(*args, **kwargs):
            try:
                func(*args, **kwargs)
                print('Intentamos hacer esto')
            except Exception as e:
                descr = 'fallo funcion causada por {:}'.format(e)
                print(descr)
        return handle_error

    @art_deco
    def launch_alert(self):
        """lanza un error cualquiera"""
        raise KeyError('oops')

    @art_deco
    def normal_func(self):
        """usa atributos del propio objeto"""
        k = 'cute_cat Dice {:}'.format(self.nya)
        print(k)


if __name__ == '__main__':
    neko = bad_cat()  # crear instancia
    neko.launch_alert()  # lanzar una funcion con error
    neko.normal_func()  # lanzar una funcion que usa atributos del objeto