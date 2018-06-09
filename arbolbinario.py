class Nodo_ab:
	def __init__(self,nom,ape,tel,mail):
		self.nom=nom
		self.ape=ape
		self.tel=tel
		self.mail=mail
		#self.next=None
		#self.prev=None
		self.right=None
		self.left=None
		self.parent=None
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
class Arbol_b():
	def __init__(self):
		self.root=None
	def empty(self):
		if(self.root is None):
			return(True)
		return(False)
	def get_root(self):
		return(self.root)
	def add(self,nom,ape,tel,mail,nodo):
		nombre=nom+ape
		if(nombre<nodo.get_nombre()):
			if(nodo.left!=None):
				self.add(nom,ape,tel,mail,nodo.left)
			else:
				nodo.left=Nodo_ab(nom,ape,tel,mail)
				nodo.left.parent=nodo
		else:
			if(nodo.right!=None):
				self.add(nom,ape,tel,mail,nodo.right)
			else:
				nodo.right=Nodo_ab(nom,ape,tel,mail)
				nodo.right.parent=nodo
	def add_1(self,nom,ape,tel,mail):
		if(self.root is None):
			nodo=Nodo_ab(nom,ape,tel,mail)
			self.root=nodo
		else:	
			self.add(nom,ape,tel,mail,self.root)
	def _find(self,nom,ape,nodo):
		nombre=nom+ape
		if(nodo==None):
			return nodo
		elif nombre == nodo.get_nombre():
			return nodo
		elif nombre<nodo.get_nombre() and nodo.left!=None:
			return self._find(nom,ape,nodo.left)
		elif nombre>nodo.get_nombre() and nodo.right!=None:
			return self._find(nom,ape,nodo.right)
	def find(self,nom,ape):
		if self.empty():
			return None
		else:
			return self._find(nom,ape,self.root)
	def in_order(self, nodo):
		if nodo==None:
			pass
		else:
			self.in_order(nodo.left)
			print(nodo.get_nom(),nodo.get_ape(),nodo.get_tel(),nodo.get_mail())
			self.in_order(nodo.right)
	def pre_order(self,nodo):
		if nodo==None:
			pass
		else:
			print(nodo.get_nom(),nodo.get_ape(),nodo.get_tel(),nodo.get_mail())
			self.pre_order(nodo.left)
			self.pre_order(nodo.right)
	def pos_order(self,nodo):
		if nodo==None:
			pass
		else:
			self.pos_order(nodo.left)
			self.pos_order(nodo.right)
			print(nodo.get_nom(),nodo.get_ape(),nodo.get_tel(),nodo.get_mail())

	def print_contacto(self,nom,ape):
		con=self.find(nom,ape)
		if(con is None):
			print("contacto inexistente")
			return(False)
		else:
			print(con.get_nom(),con.get_ape(),con.get_tel(),con.get_mail())
			return(True)
arbol=Arbol_b()
arbol.add_1("d","moreno",78743,"dani@mail.com")
arbol.add_1("a","morenoSeaT:V→Wuna  aplicaci  ́on  lineal  y  sea{v1,  .  .  .  ,  vn}  ⊂Vun  conjunto  de  vectorestales  que{T(v1),  .  .  .  ,  T(vn)}es  linealmente  independiente.  Demuestre  que{v1,  .  .  .  ,  vn}es  linealmente  independiente",75432,"dasdi@mail.com")
arbol.add_1("n","moreno",7543,"dasdi@mail.com")
arbol.add_1("i","moreno",787323,"dafdi@mail.com")
arbol.in_order(arbol.get_root())
print("-------------------------")
#arbol.pre_order(arbol.get_root())
#print("-------------------------")
#arbol.pos_order(arbol.get_root())
retorno=(arbol.find("d","moreno"))
arbol.print_contacto("d","moreno")