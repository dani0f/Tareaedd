from faker import Faker
from listadoble import Lista_s
from listadoble import Nodo
from time import time
class Hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
    self.arr=Lista_s()
  def str2num(self,key):
    return sum([ord(c) for c in key])
  def hashstr(self,key,size):
    return self.str2num(key)%size
  def put(self,nom,ape,tel,mail):
    self.arr._insertar(nom,ape,tel,mail)
    pos = self.hashstr(ape,self.size)
    if self.list[pos] is not None:
      #Si existe esa cola solo la agrego ahi
      self.list[pos]._insertar(nom,ape,tel,mail)
    else:
      #Si no existe creo una cola y lo agrego
      self.list[pos]=Lista_s()
      self.list[pos]._insertar(nom,ape,tel,mail)
  def H_buscar(self,ape):
    pos = self.hashstr(ape,self.size)
    if self.list[pos] is not None:#si existe
      aux=self.list[pos]
      return(aux.buscar(ape))
    else:
      return(None)
  def H_imprimir_contacto(self,ape):
    nod=self.H_buscar(ape)
    if(nod==None):
      return(print("contacto inexistente"))
    else:
      return(print(nod.get_nom(),nod.get_ape(),nod.get_tel(),nod.get_mail()))
  def H_eliminar(self,ape):
    if(self.H_buscar(ape) is None):
      return("inexistente")
    else:
      self.arr.eliminar(ape)
      pos = self.hashstr(ape,self.size)
      if self.list[pos] is not None:#si existe
        aux=self.list[pos]
        aux.eliminar(ape)
        return(print("eliminado"))
      else:
        return(False)
  def H_imprimir_todo(self):
    self.arr.imprimir_todos()


