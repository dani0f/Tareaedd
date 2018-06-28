class Nodo:
	def __init__(self,apellido):
		self.apellido=apellido
	def get_apellido(self):
		return(self.apellido)
class Arreglo_Nodo:
	def __init__(self):
		self.nodos=[]
		self.parent=None
		self.izq=None
		self.med=None
		self.der=None
		self.punteros=0
	def get_punteros(self):
		return(self.punteros)
	def add_nodo(self,nodo,parent):#retorna true si se desborda
		apellido=nodo.get_apellido()
		self.parent=parent
		if(len(self.nodos)==0):
			self.nodos.append(nodo)
			return(False)
		if(len(self.nodos)==1):
			self.nodos.append(nodo)
			if(apellido<self.nodos[0].get_apellido()):
				self.nodos[1]=self.nodos[0]
				self.nodos[0]=nodo
			return(False)
		if(len(self.nodos)==2):#AQUI SE DESBORDA
			self.nodos.append(nodo)
			if(self.nodos[0].get_apellido()<apellido and apellido<self.nodos[1].get_apellido()):
				self.nodos[2]=self.nodos[1]
				self.nodos[1]=nodo
			if(apellido<self.nodos[0].get_apellido()):
				self.nodos[2]=self.nodos[1]
				self.nodos[1]=self.nodos[0]
				self.nodos[0]=nodo
			return(True)
	def mostrar_nodos(self):
		for i in range(len(self.nodos)):
			print(self.nodos[i].get_apellido())
class Arbol_23():
	def __init__(self):
		self.root=None
	def get_root(self):
		return(self.root)
	def add(self,apellido):
		nodo=Nodo(apellido)
		if(self.root is None):
			arr=Arreglo_Nodo()
			arr.add_nodo(nodo,None)
			self.root=arr
		else:
			parent,arr=self.where_add(apellido,None,self.root)
			bool=arr.add_nodo(nodo,parent)
			if(bool==True):#se desbordo
				self.desbordado(arr)
	def desbordado_2(self,arr):
		parent=arr.parent
		raiz=arr.nodos[1]
		if(arr.izq is not None):
			lado_izq=arr.izq
		else:
			lado_izq=arr.nodos[0]
		if(arr.der is not None):
			lado_der_arr.der
		else:
			lado_der=arr.nodos[2]
		nueva_raiz=self.sub_arbol(lado_izq,raiz,lado_der)
		if(parent is None):
			print("el desbordado converge en la raiz")
			print("reemplazo el sub arbol como el nuevo arbol")
			self.root=nueva_raiz
		nod=nueva_raiz.nodos[0]
		parent.add_nodo(nod,parent.parent)
		print("agrego el valor de la nueva raiz en el parent")
		if(len(parent.nodos)==2):
			print("converge dentro de el arbol")
			if(nod==parent.nodos[0]):
				print("se reordena lado izq y mantiene el derecho")
				parent.izq=lado_izq
				parent.med=lado_der
			if(nod==parent.nodos[1]):
				parent.der=lado_der
				parent.med=lado_med
				print("se reordena lado der y se mantiene el izq")
		if(len(parent.nodos)==3):
			print(" el padre tambien causa desborde")
			print("lo mando a desborde para que se haga un sub arbol")
			if(parent.der==arr):
				parent.der=None
			if(parent.med==arr):
				parent.med=None
			if(parent.izq==arr):
				parent.izq=None
			izq_parent,der_parent=self.desbordado_2(self,parent)
			if(izq_parent.nodos[0]>lado_izq and izq_parent.nodos[0]<lado_der):
				izq_parent.izq=lado_izq
				izq_parent.der=lado_der
			else:
				der_parent.izq=lado_izq
				der_parent.der=lado_der
			return(lado_izq,lado_der)

	def add_sub_arbol(self,lado_izq,raiz,lado_der):
		nod_raiz=raiz.nodos[0]
		arr=Arreglo_Nodo()
		arr.add_nodo(nod_raiz,None)
		arr.izq=lado_izq
		arr.der=lado_der
		arr.punteros=2
		return(arr)
	def where_add(self,apellido,parent,arr):
		cant_punteros=arr.get_punteros()
		if(cant_punteros==0):
			return(parent,arr)
		if(cant_punteros==2):#tiene que ir a la iz?
			if(apellido < arr.nodos[0].get_apellido()):
				return(self.where_add(apellido,arr,arr.izq))
			else:#tiene que ir a la derecha?
				return(self.where_add(apellido,arr,arr.der))
		if(cant_punteros==3):
			if(apellido < arr.nodos[0].get_apellido()):
				return(self.where_add(apellido,arr,arr.izq))#tiene que ir a la iz
			if(arr.nodos[0].get_apellido()<apellido and apellido<arr.nodos[1].get_apellido()):
				return(self.where_add(apellido,arr,arr.med))#tiene que ir a almedio
			if(apellido > arr.nodos[1].get_apellido()):
				return(self.where_add(apellido,arr,arr.der))#tiene que ir a la dere
	def pre_order(self,arr):
		if arr==None:
			pass
		else:
			print("lvl------------")
			arr.mostrar_nodos()
			self.pre_order(arr.izq)
			self.pre_order(arr.med)
			self.pre_order(arr.der)
arbol=Arbol_23()
#ARBOL 1
arr_1=Arreglo_Nodo()
arr_2=Arreglo_Nodo()
arr_3=Arreglo_Nodo()
arr_4=Arreglo_Nodo()
arr_1.add_nodo(Nodo(7),None)
arr_2.add_nodo(Nodo(9),arr_1)
arr_3.add_nodo(Nodo(8),arr_2)
arr_4.add_nodo(Nodo(10),arr_2)
arr_1.der=arr_2
arr_2.der=arr_4
arr_2.izq=arr_3
arr_2.punteros=2
arr_1.punteros=1#der
#ARBOL 2
arr_11=Arreglo_Nodo()
arr_22=Arreglo_Nodo()
arr_33=Arreglo_Nodo()
arr_11.add_nodo(Nodo(5),None)
arr_22.add_nodo(Nodo(6),arr_11)
arr_33.add_nodo(Nodo(4),arr_11)
arr_11.der=arr_22
arr_11.izq=arr_33
arr_11.punteros=2
#arbol 1+2
sub_a=arbol.add_sub_arbol(arr_11,arr_1,arr_1.der)
sub_a.izq.izq.mostrar_nodos()
sub_a.mostrar_nodos()
sub_a.der.mostrar_nodos()
#pos.mostrar_nodos()
