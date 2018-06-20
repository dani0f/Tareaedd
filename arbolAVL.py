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
	def empty(self):
		if(self.root==None):
			return(True)
		return(False)
	def get_root(self):
		return(self.root)
	def add(self,nombre):
		if(self.empty()):
			nodo=Nodo(nombre)
			self.root=nodo
			#print("se agrega en la raiz")
			return(False)
		else:
			if(self.find(nombre) is not None):
				print("contacto existente")
				return("True")
			self._add(nombre,self.root)
			self.in_order_balanced(self.root)
			nodo=self.is_balanced(self.root)
			if(nodo==None):
				return(False)
			else:
				self._rotacion(nodo)#mando a rotar
				self.in_order_balanced(self.root)
				ver=self.is_balanced(self.root)
				if(ver==None):
					print("rebalanceado con exito")
					return(True)
				else:
					print("error")
					return(False)
	def _add(self,nombre,nodo):
		if(nombre<nodo.get_nombre()):
			if(nodo.left!=None):
				self._add(nombre,nodo.left)
			else:
				nodo.left=Nodo(nombre)
				nodo.left.parent=nodo
		else:
			if(nodo.right!=None):
				self._add(nombre,nodo.right)
			else:
				nodo.right=Nodo(nombre)
				nodo.right.parent=nodo
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
	def is_balanced(self,nodo):
		if(nodo is None):
			return None
		ver=self._balanceo(nodo)
		if(ver==None):
			return(None)
		else:
			if(ver.right is not None):
				if(ver.right.get_factor()==2 or ver.right.get_factor()==-2):
					ver=ver.right
			if(ver.left is not None):
				if(ver.left.get_factor()==2 or ver.left.get_factor()==-2):
					ver=ver.left
			return(ver)
	def _find(self,nombre,nodo):
		if(nodo==None):
			return nodo
		elif nombre == nodo.get_nombre():
			return nodo
		elif nombre<nodo.get_nombre() and nodo.left!=None:
			return self._find(nombre,nodo.left)
		elif nombre>nodo.get_nombre() and nodo.right!=None:
			return self._find(nombre,nodo.right)
	def find(self,nombre):
		if self.empty():
			return None
		else:
			return self._find(nombre,self.root)
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
		#		print("--con hijos")
				D1.parent=B	
			return
		C.left=B	
		#caso 1 p.factor<0 
		if(A.get_factor()<0):
			A.right=C
		#caso 2 p.factor>0 
		if(A.get_factor()>0):
			A.left=C
		C.parent=A
		B.parent=C
	def rotacion_R(self,nodo,parent):
		#print("rotacion a R desde ", nodo.get_nombre())
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
			#	print("--con hijos")
				D1.parent=B
			return
		C.right=B	
		#caso 1 p.factor<0 
		if(A.get_factor()<0):
			A.right=C
			#print("caso 1")
		#caso 2 p.factor>0 
		if(A.get_factor()>0):
			A.left=C
			#print("caso 2")
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
			print(nodo.get_nombre())
			self.in_order(nodo.right)
	def post_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.post_order(nodo.left)
			self.post_order(nodo.right)
			print(nodo.get_nombre())
avl=Avl()
avl.add(30)
avl.add(25)
avl.add(40)
avl.add(27)
avl.add(15)
avl.add(29)
avl.add(5)
avl.add(54)
avl.add(17)
avl.add(17)
avl.add(27)
avl.add(15)
avl.add(29)
avl.add(5)
avl.add(54)
avl.add(17)
avl.add(17)
avl.add(73)

avl.in_order(avl.get_root())
bool=avl.find(17)
if(bool is not None):
	print("nombre",bool.parent.get_nombre())
else:
	print("no encontrado")
#avl.pre_order(avl.get_root())
















