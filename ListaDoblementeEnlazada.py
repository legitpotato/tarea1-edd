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

    def insertarContactoLista(self,nombre,apellido,telefono,email):                     #INSERTAR CONTACTO
        nuevoContacto = Contacto(nombre,apellido,telefono,email)
    
        if nuevoContacto.apellido[0] == None:                                           #Debe introducirse al menos 1 letra
            print("Apellido no valido")
            return
    
        if self.head == None:                                                           #Si la lista esta vacia se introduce el nuevo contacto a la cabeza de inmediato
            self.head = nuevoContacto
            return
        
        aux = self.head                                                                 #Primero el auxiliar toma el valor de la cabeza.
        if aux.apellido[0] > nuevoContacto.apellido[0]:                                 #Esta linea de codigo compara las primeras letras segun el codigo ASCII, las letras del alfabeto estan ordenadas de menor a mayor, de la A a la Z.
            nuevoContacto.next = aux                                                    #Las siguientes lineas de codigo reajustaran los punteros para que el nuevo contacto quede a la cabeza con orden alfabetico.
            aux.prev = nuevoContacto                                                   
            aux.next = self.head.next                                                   
            self.head.next.prev = aux
            self.head = nuevoContacto
            return
    
        while aux != None:                                                              #En caso de que el apellido del nuevo contacto deba fijar el contacto en medio de la lista se leeran las siguientes lineas de codigo
                if aux.next.apellido[0] > nuevoContacto.apellido[0]:
                    nuevoContacto.next = aux.next
                    aux.next.prev = nuevoContacto
                    aux.next = nuevoContacto
                    nuevoContacto.prev = aux
                
                elif aux.next == None:
                    aux.next = nuevoContacto
     
                aux = aux.next                                                          #El ciclo while seguira recorriendose mientras el auxiliar ira recorriendo la lista dentro buscando el contacto que tenga una letra de menor valor ASCII, asi el nuevo contacto podra ser introducido
        return

    def buscarContactoLista(self,Contacto):                                             #BUSQUEDA CONTACTO
        if self.head == Contacto:                                                       #Si la cabeza de la lista es el contacto que se esta buscando retorna el contacto
            print("Contacto encontrado.")
            return(self.head)

        else:                                                                           #Si no se cumple la condicion anterior entonces
            aux = self.head
            while aux.next != None:                                                     #Se iniciara un ciclo y se recorrera la lista con un auxiliar hasta que el auxiliar, que apuntara al contacto en la lista, coincidad con el contacto buscado.
                if aux == Contacto:
                    print("Contacto encontrado.")
                    return(aux)
                else:
                    print("Contacto encontrado.")
                    return(aux.next)
                
            
    def borrarContactoLista(self,Contacto):                                             #BORRAR CONTACTO
        if self.head.apellido == Contacto.apellido:                                     #Si la cabeza de la lista corresponde al contacto buscado para borrar, se borrara el contacto y se reajusta la cabeza.
            self.head = self.head.next
        
        else:
            aux = self.head
            auxNext = aux.next
        
            while auxNext != None:                                                      #En caso contrario se iniciara un ciclo para buscar el contacto iterando nuevamente con auxiliares
                if auxNext.apellido == Contacto.apellido:                               #Se utilizan 2 auxiliares para reajustar bien los punteros prev y next
                    if auxNext.next == None:
                        aux.next = None
                    
                    else:
                        aux.next = auxNext.next
                        auxNext.next.prev = aux
                    
                aux = auxNext
                auxNext = aux.next


    def imprimirLibreta(self):                                                          #IMPRIMIR LIBRETA
        aux = self.head                                                                 #De la misma forma que se iteraba en la busqueda, solo que esta vez se irá imprimiendo todo lo que se encuentre
        while aux != None:
            print("Nombre: " + aux.nombre)
            print("Apellido: " + aux.apellido)
            print("------------------------------------")
