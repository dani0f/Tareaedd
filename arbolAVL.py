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
	def _balanceo(self,nodo):
		if(nodo==None):
			return(None)
		else:
			factor=nodo.get_factor()
			if(factor==2 or factor==-2):
				print(factor,nodo.get_nombre())
				return(nodo)
			else:
				a=self._balanceo(nodo.left)
				b=self._balanceo(nodo.right)
		if(a is not None):
			return(a)
		if(b is not None):
			return(b)		
		return(None)
	def in_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order(nodo.left)
			print(nodo.get_nom(),nodo.get_ape(),nodo.get_tel(),nodo.get_mail())
			self.in_order(nodo.right)
	def in_order_balanced(self,nodo):
		if nodo==None:
			pass
		else:
			self.in_order_balanced(nodo.left)
			nodo._factor()
			self.in_order_balanced(nodo.right)
	def tipo_rotacion(self,nodo):
		if(nodo.get_factor()==-2):
			nod=nodo.right.get_factor()
			if(nod==-1):
				return("L")
			if(nod==1):
				return("RL")
		if(nodo.get_factor()==2):
			nod=nodo.left.get_factor()
			if(nod==-1):
				return("LR")
			if(nod==1):
				return("R")
	
#ARBOL RR
# A=Nodo("A")
# B2=Nodo("B2")
# B=Nodo("B")
# C=Nodo("C")
# D=Nodo("D")
# A.right=B
# A.left=B2
# B.right=C
# C.right=D
# A._factor(A)
#ARBOL NORMAL
A=Nodo("A")
B1=Nodo("B1")
B=Nodo("B")
C1=Nodo("C1")
C2=Nodo("C2")
C=Nodo("C")
D=Nodo("D")
A.right=B
A.left=B1
B.left=C
C.left=D
B1.left=C1
B1.right=C2
# A._factor()
# print("A",A.get_factor())
# B1._factor()
# print("b1",B1.get_factor())
# B._factor()
# print("B",B.get_factor())
# C._factor()
# print("C",C.get_factor())
# C1._factor()
# print("c1",C1.get_factor())
# D._factor()
# print("D",D.get_factor())
avl=Avl()
avl.in_order_balanced(A)
a=avl._balanceo(A)
if(a==None):
	print("es none")
else:
	print(a.get_nombre())
rot=avl.tipo_rotacion(a)
print(rot)

















