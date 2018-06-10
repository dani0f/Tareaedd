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
	def es_hoja(self):
		if(self.profundidad==0):
			return(True)
		else:
			return(False)
	def comparador(self,con,A):#Retorna profundidad mayor
		if(A.right is None and A.left is None):
			print("es una hoja")
			return(con)
		L=self._factor_L(0,A)
		R=self._factor_R(0,A)
		if(R==L):
			print("sigo con izquierda__ +1")
			a=self.comparador(con+1,A.left)
			print("me devuelvo")
			print("sigo con derecha__ +1")
			b=self.comparador(con+1,A.right)
			print(a,b,"fin")
			if(a<b):
				#print("R es mayor") ## se retorna el mayor
				return(b)
			if(a>b):
				#print("L es mayor") ## se retorna el mayor
				return(a)
		else:
			if(R>L):
				print("sigo con derecha +1")
				con=con+1
				R=self.comparador(con,A.right)
			else:
				print("sigo con izquierda +1")
				con=con+1
				L=self.comparador(con,A.left)
				print("l",L)
			return(con)
	def _factor(self,A):
		r=self.comparador(0,A.right)
		l=self.comparador(0,A.left)
		print("valor de la derecha es",r+1)
		print("valor de la izquierda es",l+1)


	def _factor_R(self,contador_r,nodo):# devuelve profundidad de derecha
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
#C3=Nodo("C3")
C=Nodo("C")
D=Nodo("D")
A.right=B
A.left=B2
#B2.left=C3
B.right=C
B.left=C2
C2.right=D
a=A._factor(A)
















