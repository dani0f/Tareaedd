from listadoble import Lista_s
from listadoble import Nodo
class Hash:
  def __init__(self,size):
    self.list = [None]*size
    self.size= size
    self.arr=[]
  def str2num(self,key):
    return sum([ord(c) for c in key])
  def hashstr(self,key,size):
    return self.str2num(key)%size
  def put(self,nom,ape,tel,mail):
    self.arr.append(ape)
    pos = self.hashstr(ape,self.size)
    if self.list[pos] is not None:
      #Si existe esa cola solo la agrego ahi
      print(self.list[pos]._insertar(nom,ape,tel,mail))
    else:
      #Si no existe creo una cola y lo agrego
      self.list[pos]=Lista_s()
      print(self.list[pos]._insertar(nom,ape,tel,mail))
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
      pos = self.hashstr(ape,self.size)
      if self.list[pos] is not None:#si existe
        aux=self.list[pos]
        aux.eliminar(ape)
        return(print("eliminado"))
      else:
        return(False)
  def H_imprimir_todo(self):
    self.arr.sort()
    for i in range(len(self.arr)):
      print(self.arr[i])
    return
hashi=Hash(100)
hashi.put("marlin","lenzi",43242,"mail.com")
hashi.put("romina","urrutia",43242,"mail.com")
hashi.put("levi","leni",43242,"mail.com")
hashi.H_imprimir_todo()
#print("Hash importado")
