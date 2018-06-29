from faker import Faker
class Nodo:
  def __init__(self,nom,ape,tel,mail):
    self.nom=nom
    self.ape=ape
    self.tel=tel
    self.mail=mail
    self.next=None
    self.prev=None
  def get_nom(self):
    return(self.nom)
  def get_ape(self):
    return(self.ape)
  def get_tel(self):
    return(self.tel)
  def get_mail(self):
    return(self.mail)
  def get_nombre(self):
    nombre=self.get_nom()+self.get_ape()
    return(nombre)
class Lista_s:
  def __init__(self):
    self.head=None
    self.last=None
    self.cout=0
  def get_tam(self):
    return(self.cout)
  def _insertar(self,nom,ape,tel,mail):
    self.cout=self.cout+1
    nodo=Nodo(nom,ape,tel,mail)
    if(self.head is None):
      self.head=self.last=nodo
      return("agregado caso 1")
    if(self.buscar(ape) is not None):
    	pos=self.buscar(ape)
    	pos.nom=nom
    	pos.tel=tel
    	pos.mail=mail
    	self.cout=self.cout-1
    else:
      pos=self.head
      if(pos.next is None and ape<pos.get_ape()):#se agrega antes de pos
        nodo.next=pos
        pos.prev=nodo
        self.head=nodo
        self.last=pos
        return("agregado caso 2.1 fdfdsfd")
      if(pos.next is None and ape>pos.get_ape()):#se agrega despues de pos
        pos.next=nodo
        nodo.prev=pos
        self.head=pos
        self.last=nodo
        return("agregado caso 2.2")
      while(pos.next is not None):
        if(ape<pos.get_ape()):#se agrega antes de pos
          if(pos.prev is None):
            nodo.next=pos
            pos.prev=nodo
            self.head=nodo
            return("agregado a caso 3.0")
          else:
            pos.prev.next=nodo
            nodo.prev=pos.prev
            nodo.next=pos
            pos.prev=nodo
            return("agregado a caso 3.1") 
        pos=pos.next
      #se agrega despues de pos y el last cambia
      pos.next=nodo
      nodo.prev=pos
      self.last=nodo
      return("agregado a caso 4")
  def buscar(self,ape):
    pos=self.head
    if(pos is None):
      return (None)
    else:
      while(pos.next is not None):
        if(pos.get_ape()==ape):
          return(pos)
        pos=pos.next
      if(pos.get_ape()==ape):
        return(pos)
      else:
        return(None)
  def eliminar(self,ape):
    if(self.head is None):
      return("lista vacia")
    if(self.buscar(ape)):
      pos=self.head
      if(pos.get_ape()==ape):
        if(pos.next is None):
          self.head=self.last=None
          return("eliminado por 0")
        else:
          pos.next.prev=None
          self.head=pos.next
          return("eliminado por 1")
      while(pos.next!=None):
        if(pos.get_ape()==ape):
          pos.prev.next=pos.next
          pos.next.prev=pos.prev
          return("eliminado por 2")
        pos=pos.next
      if(pos.get_ape()==ape):
        self.last=pos.prev
        pos.prev.next=None
        return("eliminado por 3")
    else:
      return("no encontrado")
  def imprimir_todos(self):
    if(self.head is None):
      return("La lista esta vacia")
    pos=self.head
    if(pos.next is None):
      print("Nombre: ",pos.get_nom(),pos.get_ape(),pos.get_tel(),pos.get_mail())
      return
    while(pos.next is not None):
      print("Nombre: ",pos.get_nom(),pos.get_ape(),pos.get_tel(),pos.get_mail())
      pos=pos.next
    print("Nombre: ",pos.get_nom(),pos.get_ape(),pos.get_tel(),pos.get_mail())
    return
  def imprimir_contacto(self,apellido):
  	nod=self.buscar(apellido)
  	if(nod==None):
  		return(print("no encontrado"))
  	else:
  		print("contacto encontrado:")
  		return(print(nod.get_nom(),nod.get_ape(),nod.get_tel(),nod.get_mail()))

fake=Faker()
lista=Lista_s()
for i in range(100):
	nombre=fake.first_name()
	apellido=fake.last_name()
	telefono=fake.phone_number()
	mail=fake.email()
	lista._insertar(nombre.lower(),apellido.lower(),telefono,mail)
lista.imprimir_todos()