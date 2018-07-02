class Contacto:
    def __init__(self,nombre,apellido,telefono,email):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.busqueda = nombre+apellido
        self.next = None
        self.prev = None

class Libreta:
    def __init__(self):
        self.head = None
        self.length = 0

def insertarContactoLista(self,Contacto):
    nuevoContacto = Contacto(nombre,apellido,telefono.email)
    
    if nuevoContacto.apellido[0] == None:
        print("Apellido no valido")
        return
    
    if self.head == None:
        self.head = nuevoContacto
        
    aux = self.head
    if aux.apellido[0] > nuevoContacto.apellido[0]:
        nuevoContacto.next = aux
        aux.prev = nuevoContacto
        aux.next = self.head.next
        self.head.next.prev = aux
        self.head = nuevoContacto
        return
    
    while aux != None:
            if aux.next.apellido[0] > nuevoContacto.apellido[0]:
                nuevoContacto.next = aux.next
                aux.next.prev = nuevoContacto
                aux.next = nuevoContacto
                nuevoContacto.prev = aux
                
            elif aux.next == None:
                aux.next = nuevoContacto
     
            aux = aux.next
    return

def buscarContactoLista(self,Contacto):
    if self.head == Contacto:
        print("Contacto encontrado.")
        return(self.head)

    else:
        aux = self.head
        
        while aux.next != None:
            if aux == Contacto:
                print("Contacto encontrado.")
                return(aux)
            else:
                print("Contacto encontrado.")
                return(aux.next)
                
            
def borrarContactoLista(self,Contacto):
    if self.head.apellido == Contacto.apellido:
        self.head = self.head.next
        
    else:
        aux = self.head
        auxNext = aux.next
        
        while auxNext != None:
            if auxNext.apellido == Contacto.apellido:
                
                if auxNext.next == None:
                    aux.next = None
                    
                else:
                    aux.next = auxNext.next
                    auxNext.next.prev = aux
                    
            aux = auxNext
            auxNext = aux.next


def imprimirLibreta(self):
    aux = self.head
    while aux != None:
        print("Nombre: " + aux.nombre)
        print("Apellido: " + aux.apellido)
        print("------------------------------------")
