class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.busqueda = nombre+apellido
        self.next = None
        self.prev = None
