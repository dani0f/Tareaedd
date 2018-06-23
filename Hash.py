def str2num(key):
  return sum([ord(c) for c in key])
def hashstr(key,size):
  return str2num(key)%size
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
    else:
      pos=self.head
      if(pos.next is None and ape==pos.get_ape()):
        self.head=self.last=nodo
        return("agregado caso csao")
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
        if(ape==pos.get_ape()):
          pos.prev.next=nodo
          nodo.prev=pos.prev
          nodo.next=pos.next
          pos.next.prev=nodo
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
        posprev=pos 
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
  def imprimir_nombre(self):
    if(self.head is None):
      return("La lista esta vacia")
    pos=self.head
    if(pos.next is None):
      print("Nombre: ",pos.get_nom(),pos.get_ape())
      return
    while(pos.next is not None):
      print("Nombre: ",pos.get_nom(),pos.get_ape())
      pos=pos.next
    print("Nombre: ",pos.get_nom(),pos.get_ape())
    return
class Hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
  def put(self,nom,ape,tel,mail):
    pos = hashstr(ape,self.size)
    if self.list[pos] is not None:
      #Si existe esa cola solo la agrego ahi
      print(self.list[pos]._insertar(nom,ape,tel,mail))
    else:
      #Si no existe creo una cola y lo agrego
      self.list[pos]=Lista_s()
      print(self.list[pos]._insertar(nom,ape,tel,mail))
  def listado(self,ape):
    pos = hashstr(ape,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
      aux.imprimir_nombre()
    else:
      print("categoria no encontrada")
  def H_buscar(self,ape):
    pos = hashstr(ape,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
      return(aux.buscar(ape))
    else:
      return(False)
  def H_eliminar(self,ape):
    if(self.H_buscar(ape) is None):
      return("inexistente")
    else:
      pos = hashstr(ape,self.size)
      if self.list[pos] is not None:#si existe
        aux=self.list[pos]
        aux.eliminar(ape)
        return(True)
      else:
        return(False)
H=Hash(100)
H.put("aa","bb",343242,"Mail.com")
H.put("bb","bb",32342,"mai.comb")
H.put("cc","bb",32342,"mai.comb")
a=H.H_buscar("bb")
print(a)
H.H_eliminar("bb")
a=H.H_buscar("bb")
print(a)