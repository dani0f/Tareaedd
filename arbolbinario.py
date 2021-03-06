from faker import Faker
from time import time
class Nodo_ab:
	def __init__(self,nom,ape,tel,mail):
		self.nombre=nom
		self.apellido=ape
		self.telefono=tel
		self.mail=mail
		self.right=None
		self.left=None
		self.parent=None
	def get_parent(self):
		return(self.parent)
	def get_nombre(self):
		return(self.nombre)
	def get_apellido(self):
		return(self.apellido)
	def get_telefono(self):
		return(self.telefono)
	def get_mail(self):
		return(self.mail)
	def es_hoja(self):
		if(self.left is None and self.right is None):
			return(True)
		else:
			return(False)
class Arbol_b():
	def __init__(self):
		self.root=None

	def empty(self):
		if(self.root is None):
			return(True)
		return(False)
	def get_root(self):
		return(self.root)
	def _add(self,nom,ape,tel,mail,nodo):
		if(ape<nodo.get_apellido()):
			if(nodo.left!=None):
				self._add(nom,ape,tel,mail,nodo.left)
			else:
				nodo.left=Nodo_ab(nom,ape,tel,mail)
				nodo.left.parent=nodo
		else:
			if(nodo.right!=None):
				self._add(nom,ape,tel,mail,nodo.right)
			else:
				nodo.right=Nodo_ab(nom,ape,tel,mail)
				nodo.right.parent=nodo
	def add(self,nom,ape,tel,mail):
		if(self.root is None):
			nodo=Nodo_ab(nom,ape,tel,mail)
			self.root=nodo
		if(self.find(ape) is not None):
			nod=self.find(ape)
			nod.nombre=nom
			nod.telefono=tel
			nod.mail=mail
		else:	
			self._add(nom,ape,tel,mail,self.root)
	def _find(self,ape,nodo):
		if(nodo==None):
			return nodo
		elif ape == nodo.get_apellido():
			return nodo
		elif ape<nodo.get_apellido() and nodo.left!=None:
			return self._find(ape,nodo.left)
		elif ape>nodo.get_apellido() and nodo.right!=None:
			return self._find(ape,nodo.right)
	def find(self,ape):
		if self.empty():
			return None
		else:
			return self._find(ape,self.root)
	def in_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order(nodo.left)
			print(nodo.get_nombre(),nodo.get_apellido(),nodo.get_telefono(),nodo.get_mail())
			self.in_order(nodo.right)
	def pre_order(self,nodo):
		if nodo==None:
			pass
		else:
			print(nodo.get_nombre(),nodo.get_apellido(),nodo.get_telefono(),nodo.get_mail())
			self.pre_order(nodo.left)
			self.pre_order(nodo.right)
	def pos_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.pos_order(nodo.left)
			self.pos_order(nodo.right)
			print(nodo.get_nombre(),nodo.get_apellido(),nodo.get_telefono(),nodo.get_mail())
	def print_contact(self,ape):
		con=self.find(ape)
		if(con is None):
			return(print("*contacto inexistente"))
		else:
			print("*contacto encontrado*")
			return(print(con.get_nombre(),con.get_apellido(),con.get_telefono(),con.get_mail()))
	def delete(self,ape):
		if self.empty():
			return(None)
		nod=self.find(ape)	
		if(nod is None):
			return(print("inexistente"))
		else:
			return self._delete(self.find(ape))
	def _delete(self,node):
		def max_apellido(nodo):
			pos=nodo
			while(pos.right != None):
				pos=pos.right
			return (pos)
		def min_apellido(nodo):
			pos=nodo
			while(pos.left != None):
				pos=pos.left
			return (pos)
		def n_hijos(nodo):
			n_hijos=0
			if(nodo.left != None):
				n_hijos+=1
			if(nodo.right != None):
				n_hijos+=1
			return (n_hijos)
		node_parent = node.parent
		node_children = n_hijos(node)
		if node_children == 0:
			if(node_parent is None):#raiz sin hijos
				self.root=None
				return
			if node_parent.left == node:
				node_parent.left = None
			else:
				node_parent.right = None
		if node_children == 1:
			if(node_parent is None and node.right != None):#raiz con 1 hijo
				der=self.root.right
				izq=None
				nueva_raiz=min_apellido(node.right)
				if(der==nueva_raiz):
					nueva_raiz.right=der.right
					nueva_raiz.left=None
					nueva_raiz.parent=None
					self.root=nueva_raiz
				else:
					nueva_raiz.parent.left=None
					nueva_raiz.right=der
					nueva_raiz.left=izq
					nueva_raiz.parent=None
					self.root=nueva_raiz
				return
			if(node_parent is None and node.left != None):#raiz con 1 hijo
				izq=self.root.left
				der=None
				nueva_raiz=max_apellido(node.left)
				if(izq==nueva_raiz):
					nueva_raiz.left=izq.left
					nueva_raiz.right=izq.right
					nueva_raiz.parent=None
					self.root=nueva_raiz
				else:
					nueva_raiz.parent.right=None
					nueva_raiz.left=izq
					nueva_raiz.right=der
					nueva_raiz.parent=None
					self.root=nueva_raiz
				return
			if node.left != None:
				child = node.left
			else:
				child = node.right
			if node_parent.left == node:
				node_parent.left = child
			else:
				node_parent.right = child
			child.parent = node_parent
		if node_children == 2:
			if(node_parent is None and node.right != None):#raiz con 1 hijo
				nueva_raiz=min_apellido(node.right)
				der=self.root.right
				izq=self.root.left
				nueva_raiz=min_apellido(node.right)
				if(der==nueva_raiz):
					nueva_raiz.right=der.right
					nueva_raiz.left=izq
					nueva_raiz.parent=None
					self.root=nueva_raiz
				else:
					nueva_raiz.parent.left=None
					nueva_raiz.right=der
					nueva_raiz.left=izq
					nueva_raiz.parent=None
					self.root=nueva_raiz
				return
			successor = min_apellido(node.right) #sucesor in order del que sera eliminado 
			node.nombre = successor.nombre
			node.apellido = successor.apellido  
			self._delete(successor)
# arbol=Arbol_b()
# fake=Faker()
# inicio=time()
# array=list()
# for i in range(100):
# 	nombre=fake.first_name()
# 	apellido=fake.last_name()
# 	telefono=fake.phone_number()
# 	mail=fake.email()
# 	arbol.add(nombre.lower(),apellido.lower(),telefono,mail)
# 	array.append(apellido.lower())
# inicio=time()
# for p in range(100):
#   apellido=array[p]
#   arbol.find(apellido)
# final=time()
# print(final-inicio)
