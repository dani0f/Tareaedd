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
		if(self.buscar(nom,ape) is not None):
			return("contacto existente")
		else:
			nombre=nom+ape
			pos=self.head
			if(pos.next is None and nombre<pos.get_nombre()):#se agrega antes de pos
				nodo.next=pos
				pos.prev=nodo
				self.head=nodo
				self.last=pos
				return("agregado caso 2.1 fdfdsfd")
			if(pos.next is None and nombre>pos.get_nombre()):#se agrega despues de pos
				pos.next=nodo
				nodo.prev=pos
				self.head=pos
				self.last=nodo
				return("agregado caso 2.2")
			while(pos.next is not None):
				if(nombre<pos.get_nombre()):#se agrega antes de pos
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
	def buscar(self,nom,ape):
		nombre=nom+ape
		pos=self.head
		if(pos is None):
			return (None)
		else:
			while(pos.next is not None):
				if(pos.get_nombre() ==nombre):
					return(True)
				pos=pos.next
			if(pos.get_nombre()==nombre):
				return(True)
			else:
				return(None)
	def eliminar():
		print("elimina un nodo")
	def imprimir(self,nom=True,ape=True,tel=True,mail=True):
		if(self.head is None):
			return("La lista esta vacia")
		pos=self.head
		if(pos.next is None):
			if(nom):print("Nombre: ",pos.get_nom())
			if(ape):print("Apellido:",pos.get_ape())
			if(tel):print("Telefono:",pos.get_tel())
			if(mail):print("Mail:",pos.get_mail())
			return
		while(pos.next is not None):
			if(nom):print("Nombre: ",pos.get_nom())
			if(ape):print("Apellido:",pos.get_ape())
			if(tel):print("Telefono:",pos.get_tel())
			if(mail):print("Mail:",pos.get_mail())
			pos=pos.next
		if(nom):print("Nombre: ",pos.get_nom())
		if(ape):print("Apellido:",pos.get_ape())
		if(tel):print("Telefono:",pos.get_tel())
		if(mail):print("Mail:",pos.get_mail())
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
	def eliminar(self,nom,ape):
		nombre=nom+ape
		if(self.head is None):
			return("lista vacia")
		if(self.buscar(nom,ape)):
			pos=self.head
			if(pos.get_nombre()==nombre):
				if(pos.next is None):
					self.head=self.last=None
					return("eliminado por 0")
				else:
					pos.next.prev=None
					self.head=pos.next
					return("eliminado por 1")
			while(pos.next!=None):
				if(pos.get_nombre()==nombre):
					pos.prev.next=pos.next
					pos.next.prev=pos.prev
					return("eliminado por 2")
				pos=pos.next
			if(pos.get_nombre()==nombre):
				self.last=pos.prev
				pos.prev.next=None
				return("eliminado por 3")
		else:
			return("no encontrado")



#contacto=Nodo("maria","montes",4545,"maria.montes@gmail.com")
lista=Lista_s()
print(lista._insertar("c","c",4545,"maria.montes@gmail.com"))
print(lista._insertar("c","d",4545,"maria.montes@gmail.com"))
print(lista._insertar("c","c",4545,"maria.montes@gmail.com"))
print(lista._insertar("c","d",4545,"maria.montes@gmail.com"))
print(lista._insertar("a","a",4545,"maria.montes@gmail.com"))
print(lista._insertar("a","a",4545,"maria.montes@gmail.com"))
print(lista.get_tam())
#lista.imprimir()
lista.imprimir_nombre()
print(lista.eliminar("c","c"))
print(lista.eliminar("a","a"))
print(lista.eliminar("c","d"))
print(lista._insertar("c","d",4545,"maria.montes@gmail.com"))
lista.imprimir_nombre()
