class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.busqueda = nombre+apellido
        self.next = None
        self.prev = None

def str2num(key):
  return sum([ord(c) for c in key])

def hashstr(key):
  return str2num(key)%size

class Libreta:
    def __init__(self,Contacto):
        self.lista = [None]*len(Contacto.apellido)
        self.size = len(Contacto.apellido)

    def insertarContactoLista(self,Contacto):
        nuevoContacto = Contacto(nombre,apellido,telefono.email)
        pos = hashstr(self.size)

        if self.lista[pos] != None:
        
