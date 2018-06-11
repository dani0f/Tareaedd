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
			if(a<b):
				return(b)
			if(a>b):
				return(a)
		else:
			if(R>L):
				#print("sigo con derecha +1")
				con=con+1
				#print(con)
				R=self.comparador(con,A.right)
				#print("contador R",R)
				return(R)
			else:
				#print("sigo con izquierda +1")
				con=con+1
				#print(con)
				L=self.comparador(con,A.left)
				#print("contador L",L)
				return(L)
	def _factor(self):
		if(self.es_hoja()==True):
			self.factor=0
			r=l=0
		else:
			if(self.right is not None):
				r=self.comparador(0,A.right)
				r=r+1
			else:
				r=0
			if(self.left is not None):
				l=self.comparador(0,A.left)
				l=l+1
			else:
				l=0
		self.factor=l-r
		print("valor de la derecha es",r)
		print("valor de la izquierda es",l)
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
	def balanceo(self,nodo):#retorna None si esta balanceada si no entrega el nodo desbalanceado
		# debe recorrer todo el arbol en busca de un +-2 
		# lo recorre en order
		print("jrio")
	
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
B2=Nodo("B2")
B=Nodo("B")
C2=Nodo("C2")
C3=Nodo("C3")
C=Nodo("C")
D=Nodo("D")
A.right=B
A.left=B2
B.left=C2
B.right=C
C2.right=D
A._factor()
print(A.get_factor())
















