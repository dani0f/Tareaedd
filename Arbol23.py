class Nodo:
	def __init__(self,apellido):
		self.apellido=apellido
	def get_apellido(self):
		return(self.apellido)
class Arreglo_Nodo:
	def __init__(self):
		self.nodos=[]
		self.parent=None
		self.puntero_izq=None
		self.puntero_med=None
		self.puntero_der=None
		self.cont_nodos=0
		self.cant_punteros=0
	def add_nodo(self,apellido):#retorna true si se desborda
		nodo=Nodo(apellido)
		if(self.cont_nodos==0):
			self.nodos.append(nodo)
			self.cont_nodos=self.cont_nodos+1
			return(False)
		if(self.cont_nodos==1):
			self.nodos.append(nodo)
			if(apellido<self.nodos[0].get_apellido()):
				self.nodos[1]=self.nodos[0]
				self.nodos[0]=nodo
			self.cont_nodos=self.cont_nodos+1
			return(False)
		if(self.cont_nodos==2):#AQUI SE DESBORDA
			self.nodos.append(nodo)
			if(self.nodos[0].get_apellido()<apellido and apellido<self.nodos[1].get_apellido()):
				self.nodos[2]=self.nodos[1]
				self.nodos[1]=nodo
			if(apellido<self.nodos[0].get_apellido()):
				self.nodos[2]=self.nodos[1]
				self.nodos[1]=self.nodos[0]
				self.nodos[0]=nodo
			self.cont_nodos=self.cont_nodos+1
			return(True)
	def mostrar_nodos(self):
		cont=self.cont_nodos
		for i in range(cont):
			print(self.nodos[i].get_apellido())
class Arbol_23():
	def __init__(self):
		self.root=None
	def add(self,apellido):
		if(self.root is None):
			arr=Arreglo_Nodo()
			arr.add_nodo(apellido)
		else:
			med=self._add(apellido,self.root)
			if(med is not None):
				self.desbordado(med)
	def _add(self,apellido,nodo):
		tam=len(nodo)
		if(len==0):
			#lo agrego aca en un nuevo nodo
		if(len==1):
			
		if(len==2):
		



		
arr=Arreglo_Nodo()
arr.add(5)
arr.add(2)
arr.add(7)
arr.mostrar_nodos()
