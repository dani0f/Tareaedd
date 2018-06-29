from faker import Faker
from time import time
class Nodo_A:
	def __init__(self,nom,ape,tel,mail):
		self.nombre=nom
		self.apellido=ape
		self.telefono=tel
		self.mail=mail
		self.right=None
		self.left=None
		self.parent=None
		self.factor=0
	def get_right(self):
		return(self.right)
	def get_left(self):
		return(self.left)
	def get_nombre(self):
		return(self.nombre)
	def get_apellido(self):
		return(self.apellido)
	def get_telefono(self):
		return(self.telefono)
	def get_mail(self):
		return(self.mail)
	def get_parent(self):
		return(self.parent)
	def get_factor(self):
		return(self.factor)
	def es_hoja(self):
		if(self.left is None and self.right is None):
			return(True)
		else:
			return(False)
	def comparador(self,con,A):
		if(A.right is None and A.left is None):
			return(con)
		L=self._factor_L(0,A)
		R=self._factor_R(0,A)
		if(R==L):
			a=self.comparador(con+1,A.left)
			b=self.comparador(con+1,A.right)
			if(a<=b):
				return(b)
			if(a>b):
				return(a)
		else:
			if(R>L):
				con=con+1
				R=self.comparador(con,A.right)
				return(R)
			else:
				con=con+1
				L=self.comparador(con,A.left)
				return(L)
	def _factor_R(self,contador_r,nodo):
		if(nodo.right is not None):
			contador_r=contador_r+1
			return(self._factor_R(contador_r,nodo.right))
		else:
			return(contador_r)
	def _factor_L(self,contador_l,nodo):
		if(nodo.left is not None):
			contador_l=contador_l+1
			return(self._factor_L(contador_l,nodo.left))
		else:
			return(contador_l)	
	def _factor(self):
		if(self.right is None and self.left is None):
			self.factor=0
			return(0)
		else:
			if(self.right is not None):
				r=self.comparador(0,self.right)
				r=r+1
			else:
				r=0
			if(self.left is not None):
				l=self.comparador(0,self.left)
				l=l+1
			else:
				l=0
		self.factor=l-r
		return(l-r)
class Avl_Tree:
	def __init__(self):
		self.root=None
	def empty(self):
		if(self.root==None):
			return(True)
		return(False)
	def get_root(self):
		return(self.root)
	def in_order_balanced(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order_balanced(nodo.left)
			nodo._factor()
			self.in_order_balanced(nodo.right)
	def add(self,nom,ape,tel,mail):
		if(self.empty()):
			nodo=Nodo_A(nom,ape,tel,mail)
			self.root=nodo
			return(False)
		if(self.find(ape) is not None):
			nod=self.find(ape)
			nod.nombre=nom
			nod.telefono=tel
			nod.mail=mail
			return("True")
		else:
			self._add(nom,ape,tel,mail,self.root)
			self.in_order_balanced(self.root)
			nodo=self.is_balanced(self.root)
			if(nodo==None):
				return(False)
			else:
				self._rotacion(nodo)#mando a rotar
				self.in_order_balanced(self.root)
				ver=self.is_balanced(self.root)
	def _add(self,nom,ape,tel,mail,nodo):
		if(ape<nodo.get_apellido()):
			if(nodo.left!=None):
				self._add(nom,ape,tel,mail,nodo.left)
			else:
				nodo.left=Nodo_A(nom,ape,tel,mail)
				nodo.left.parent=nodo
		if(ape>nodo.get_apellido()):
			if(nodo.right!=None):
				self._add(nom,ape,tel,mail,nodo.right)
			else:
				nodo.right=Nodo_A(nom,ape,tel,mail)
				nodo.right.parent=nodo
	def _balanceo(self,nodo):
		if(nodo==None):
			return(None)
		else:
			factor=nodo.get_factor()
			if(factor>=2 or factor<=-2):
				return(nodo)
			else:
				a=self._balanceo(nodo.left)
				b=self._balanceo(nodo.right)
		if(a is not None):
			return(a)
		if(b is not None):
			return(b)		
		return(None)
	def is_balanced(self,nodo):
		if(nodo is None):
			return None
		ver=self._balanceo(nodo)
		if(ver==None):
			return(None)
		else:
			if(ver.right is not None):
				if(ver.right.get_factor()>=2 or ver.right.get_factor()<=-2):
					ver=ver.right
			if(ver.left is not None):
				if(ver.left.get_factor()>=2 or ver.left.get_factor()<=-2):
					ver=ver.left
			return(ver)
	def _rotacion(self,nodo):
		if(nodo.get_factor()<0):
			nodo_right=nodo.right.get_factor()
			if(nodo_right<0):
				self.rotacion_L(nodo,nodo.get_parent())
				return("L")
			if(nodo_right>0):
				self.rotacion_RL(nodo,nodo.get_parent())
				return("RL")
		if(nodo.get_factor()>0):
			nod_left=nodo.left.get_factor()
			if(nod_left<0):
				self.rotacion_LR(nodo,nodo.get_parent())
				return("LR")
			if(nod_left>0):
				self.rotacion_R(nodo,nodo.get_parent())
				return("R")
	def rotacion_L(self,nodo,parent):
		#print("rotacion a L desde ", nodo.get_nombre())
		B=nodo 
		A=parent
		C=B.right
		B.right=None
		#caso 0 b es una raiz y no tiene parent
		if(A is None):
		#	print("se cambia la raiz")	
			D1=C.left
			C.left=B
			B.right=D1
			self.root=C
			C.parent=None
			B.parent=C
			if(D1 is not None):
				D1.parent=B	
			return
		C.left=B	
		if(A.get_factor()<0):
			A.right=C 
		if(A.get_factor()>0):
			A.left=C
		C.parent=A
		B.parent=C
	def rotacion_R(self,nodo,parent):
		B=nodo 
		A=parent
		C=B.left
		B.left=None
		#caso 0 b es una raiz y no tiene parent
		if(A is None):
			#print("se cambia la raiz")	
			D1=C.right
			C.right=B
			B.left=D1
			self.root=C
			C.parent=None
			B.parent=C
			if(D1 is not None):
				D1.parent=B
			return
		C.right=B	 
		if(A.get_factor()<0):
			A.right=C 
		if(A.get_factor()>0):
			A.left=C
		C.parent=A
		B.parent=C
	def rotacion_LR(self,nodo,parent):
		#print("rotacion a LR desde ", nodo.get_nombre())
		B=nodo
		A=parent
		C=B.left
		D=C.right
		D.left=C #primero copio C a la derecha de D
		B.left=D
		C.right=None
		D.parent=B
		C.parent=D
		self.rotacion_R(B,A)#lo mando a rotacion hacia la izquierda
		#print("rotacion a RL terminada")
	def rotacion_RL(self,nodo,parent):
		#print("rotacion a RL desde ", nodo.get_nombre())
		B=nodo
		A=parent
		C=B.right
		D=C.left
		D.right=C #primero copio C a la derecha de D
		B.right=D
		C.left=None
		D.parent=B
		C.parent=D
		self.rotacion_L(B,A)#lo mando a rotacion hacia la izquierda
		#print("rotacion a RL terminada")
	def _find(self,apellido,nodo):
		if(nodo==None):
			return nodo
		elif apellido == nodo.get_apellido():
			return nodo
		elif apellido<nodo.get_apellido() and nodo.left!=None:
			return self._find(apellido,nodo.left)
		elif apellido>nodo.get_apellido() and nodo.right!=None:
			return self._find(apellido,nodo.right)
	def find(self,apellido):
		if self.empty():
			return None
		else:
			return self._find(apellido,self.root)
	def pre_order(self,nodo):
		if nodo==None:
			pass
		else:
			print(nodo.get_nombre(),nodo.get_apellido(),)
			self.pre_order(nodo.left)
			self.pre_order(nodo.right)
	def in_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order(nodo.left)
			print(nodo.get_nombre(),nodo.get_apellido())
			self.in_order(nodo.right)
	def post_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.post_order(nodo.left)
			self.post_order(nodo.right)
			print(nodo.get_nombre(),nodo.get_apellido())
	def delete(self,ape):
		if self.empty():
			return(None)
		nod=self.find(ape)
		if(nod is None):
			return(print("no encontrado"))
		else:
			self._delete(self.find(ape))
			self.in_order_balanced(self.root)
			nodo=self.is_balanced(self.root)
			if(nodo==None):
				return("eliminado sin tener que balancear")
			else:
				self._rotacion(nodo)#mando a rotar
				self.in_order_balanced(self.root)
				ver=self.is_balanced(self.root)
				if(ver==None):
					return("eliminado y rebalanceado")
				else:
					return("eliminado no balanceado")
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
			#print("Sin hijos")
			if(node_parent is None):#raiz sin hijos
				#print("eliminando raiz")
				self.root=None
				return
			if node_parent.left == node:
				node_parent.left = None
			else:
				node_parent.right = None
		if node_children == 1:
			#print("Un hijo")
			if(node_parent is None and node.right != None):#raiz con 1 hijo
				#print("no tiene padre eliminando raiz")
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
				#print("no tiene padre eliminando raiz")
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
			#print("Dos hijos")
			if(node_parent is None and node.right != None):#raiz con 1 hijo
				#print("no tiene padre eliminando raiz")
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
				return()
			successor = min_apellido(node.right) #sucesor in order del que sera eliminado 
			node.nombre = successor.nombre
			node.apellido = successor.apellido  
			self._delete(successor)
	def print_contact(self,apellido):
		nod=self.find(apellido)
		if(nod == None):
			return(print("contacto inexistente"))
		else:
			return(print(nod.get_nombre(),nod.get_apellido(),nod.get_telefono(),nod.get_mail()))
# arbol_avl=Avl_Tree()
# fake=Faker()
# array=list()
# for i in range(20):
# 	nombre=fake.first_name()
# 	apellido=fake.last_name()
# 	telefono=fake.phone_number()
# 	mail=fake.email()
# 	arbol_avl.add(nombre.lower(),apellido.lower(),telefono,mail)
# 	array.append(apellido.lower())
# inicio=time()
# for p in range(20):
#   apellido=array[p]
#   arbol_avl.delete(apellido)
# final=time()
# print(final-inicio)
