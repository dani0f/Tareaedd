class Nodo:
	def __init__(self,nombre):
		self.nombre=nombre
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
	def get_parent(self):
		return(self.parent)
	def get_factor(self):
		return(self.factor)
	def es_hoja(self):
		if(self.left is None and self.right is None):
			return(True)
		else:
			return(False)
	def comparador(self,con,A):#Retorna profundidad mayor
		if(A.right is None and A.left is None):
			#print("es una hoja")
			return(con)
		L=self._factor_L(0,A)
		R=self._factor_R(0,A)
		if(R==L):
			#print("sigo con izquierda__ +1")
			a=self.comparador(con+1,A.left)
			#print("me devuelvo")
			#print("sigo con derecha__ +1")
			b=self.comparador(con+1,A.right)
			#print(a,b,"fin")
			if(a<=b):
				return(b)
			if(a>b):
				return(a)
		else:
			if(R>L):
			#	print("sigo con derecha +1")
				con=con+1
			#	print(con)
				R=self.comparador(con,A.right)
			#	print("contador R",R)
				return(R)
			else:
			#	print("sigo con izquierda +1")
				con=con+1
			#	print(con)
				L=self.comparador(con,A.left)
			#	print("contador L",L)
				return(L)
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
		#print(self.get_nombre(),"izq=",l,"der=",r)
		return(l-r)
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
class Avl:
	def __init__(self):
		self.root=None
	def empty():
		if(self.root==None):
			return(True)
		return(False)
	def add(self,dato):
		if(self.root is None):
			nodo=Nodo(dato)
			self.root=nodo
		else:	
			self._add(dato,self.root)
	def add(self,dato):
		if(self.empty()):
			return(False)
		else:
			self._add(dato,self.root)
			self.in_order_balanced(self.root)
			nodo=self._balanceo(self.root)
			if(nodo==None):
				return(False)
			else:
				self._rotacion(nodo)#mando a rotar
				return(True)
	def _add(self,dato,nodo):
		if(dato<nodo.get_dato()):
			if(nodo.left!=None):
				self.add(dato,nodo.left)
			else:
				nodo.left=Nodo(dato)
				nodo.left.parent=nodo
		else:
			if(hoja.right!=None):
				self.add(dato,hoja.right)
			else:
				hoja.right=Hoja(dato)
				hoja.right.parent=hoja
	def _balanceo(self,nodo):
		if(nodo==None):
			return(None)
		else:
			factor=nodo.get_factor()
			if(factor==2 or factor==-2):
				#print(factor,nodo.get_nombre())
				return(nodo)
			else:
				a=self._balanceo(nodo.left)
				b=self._balanceo(nodo.right)
		if(a is not None):
			return(a)
		if(b is not None):
			return(b)		
		return(None)
	def in_order_balanced(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order_balanced(nodo.left)
			nodo._factor()
			self.in_order_balanced(nodo.right)
	def _rotacion(self,nodo):
		if(nodo.get_factor()==-2):
			nod=nodo.right.get_factor()
			if(nod==-1):
				self.rotacion_L(nodo,nodo.get_parent())
				return("L")
			if(nod==1):
				self.rotacion_RL(nodo,nodo.get_parent())
				return("RL")
		if(nodo.get_factor()==2):
			nod=nodo.left.get_factor()
			if(nod==-1):
				self.rotacion_LR(nodo,nodo.get_parent())
				return("LR")
			if(nod==1):
				self.rotacion_R(nodo,nodo.get_parent())
				return("R")
	def pre_order(self,nodo):
		if nodo==None:
			pass
		else:
			print(nodo.get_nombre())
			self.pre_order(nodo.left)
			self.pre_order(nodo.right)
	def in_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order(nodo.left)
			#print(nodo.get_nombre())
			self.in_order(nodo.right)
	def balanceo(self):
		if(self.root is None):
			return False
		else:
			ver=self._balanceo(self.root)
			if(ver==None):
				return(False)
			else:
				return(ver)
	def balanceo_1(self,nodo):

		if(nodo is None):
			return False
		ver=self._balanceo(nodo)
		if(ver==None):
			return(False)
		else:
			if(ver.right is not None):
				if(ver.right.get_factor()==2 or ver.right.get_factor()==-2):
					ver=ver.right
			if(ver.left is not None):
				if(ver.left.get_factor()==2 or ver.left.get_factor()==-2):
					ver=ver.left
			return(ver)

	def rotacion_L(self,nodo,parent):
		print("rotacion a L")
		pass	
	def rotacion_R(self,nodo,parent):
		print("rotacion a R")
		B=nodo 
		A=parent
		C=B.left
		B.left=None
		C.right=B
		#caso 0 b es una raiz y no tiene parent
		if(A is None):
			print(" se cambia la raiz")
		#caso 1 p.factor<0 
		if(A.get_factor()<0):
			A.right=C
			print("caso 1")
		#caso 2 p.factor>0 
		if(A.get_factor()>0):
			A.left=C
			print("caso 2")
		C.parent=A
		B.parent=C
	def rotacion_LR(self,nodo,parent):
		print("rotacion a LR")
	def rotacion_RL(self,nodo,parent):
		print("rotacion a RL")
A=Nodo("A")
B1=Nodo("B1")
B=Nodo("B")
C1=Nodo("C1")
C2=Nodo("C2")
C=Nodo("C")
D=Nodo("D")
A.right=B
A.left=B1
B1.left=C
C.left=D
B.parent=A
B1.parent=A
C.parent=B1
D.parent=C
avl=Avl()
avl.in_order_balanced(A)
ver=avl.balanceo_1(A)
print("Nodo desbalanceado encontrado",ver.get_nombre())
avl.pre_order(A)
print("----------")
print("Aplicando rotacion tipo",avl._rotacion(ver))
avl.pre_order(A)
















