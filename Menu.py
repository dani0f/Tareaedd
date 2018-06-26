from listadoble import Nodo
from listadoble import Lista_s
from arbolbinario import Nodo_ab
from arbolbinario import Arbol_b
from arbolAVL import Nodo_A
from arbolAVL import Avl_Tree
from Hash import Hash
class Estructuras:	
	def __init__(self):
		self.list=Lista_s()
		self.abb=Arbol_b()
		self.avl=Avl_Tree()
		self.hash=Hash(100)
	def menu_list(self,opcion):
		if(opcion==1):#agregar contacto
			agregar_nom()
			self.list._insertar("naruto","uzumaki",43242,"mail.com")
			self.list._insertar("hinata","hyuga",43242,"mail.com")
			self.list._insertar("sasuke","uchiha",43242,"mail.com")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			self.list.eliminar("uzumaki")
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			self.list.imprimir_contacto("hyuga")
			print("----------------------------------")
			return(False)
		if(opcion==4):
			print("---Mostrando Lista de contactos---")
			self.list.imprimir_todos()
			print("----------------------------------")
			return(False)
		if(opcion==5):
			print("---exit---------------------------")
			print("saliendo de lista enlazada")
			print("----------------------------------")
			return(True)
	def menu_abb(self,opcion):
		if(opcion==1):#agregar contacto
			print("---agregar contacto---------------")
			agregar_nom()
			self.abb.add("naruto","uzumaki",43242,"mail.com")
			self.abb.add("hinata","hyuga",43242,"mail.com")
			self.abb.add("sasuke","uchiha",43242,"mail.com")
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			self.abb.delete("uchiha")
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			self.abb.print_contact("hyuga")
			print("----------------------------------")
			return(False)
		if(opcion==4):
			print("---Mostrando Lista de contactos---")
			self.abb.in_order(self.abb.get_root())
			print("----------------------------------")
			return(False)
		if(opcion==5):
			print("---exit---------------------------")
			print("saliendo de Arbol binario de busqueda")
			print("----------------------------------")
			return(True)
	def menu_avl(self,opcion):
		if(opcion==1):#agregar contacto
			print("---agregar contacto---------------")
			agregar_nom()
			self.avl.add("naruto","uzumaki",43242,"mail.com")
			self.avl.add("hinata","hyuga",43242,"mail.com")
			self.avl.add("sasuke","uchiha",43242,"mail.com")
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			self.avl.delete("uzumaki")
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			self.avl.print_contact("hyuga")
			print("----------------------------------")
			return(False)
		if(opcion==4):
			print("---Mostrando Lista de contactos---")
			self.avl.in_order(self.avl.get_root())
			print("----------------------------------")
			return(False)
		if(opcion==5):
			print("---exit---------------------------")
			print("saliendo de Arbol AVL")
			print("----------------------------------")
			return(True)	
	def menu_hash(self,opcion):
		if(opcion==1):#agregar contacto
			print("---agregar contacto---------------")
			agregar_nom()
			self.hash.put("naruto","uzumaki",43242,"mail.com")
			self.hash.put("hinata","hyuga",43242,"mail.com")
			self.hash.put("sasuke","uchiha",43242,"mail.com")
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			self.hash.H_eliminar("uzumaki")
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			self.hash.H_imprimir_contacto("hyuga")
			print("----------------------------------")
			return(False)
		if(opcion==4):
			print("---Mostrando Lista de contactos---")
			self.hash.H_imprimir_todo()
			print("----------------------------------")
			return(False)
		if(opcion==5):
			print("---exit---------------------------")
			print("saliendo de Hash")
			print("----------------------------------")
			return(True)	
def menu():
	print(" 1 para agregar contacto nuevo")
	print(" 2 para eliminar contactos")
	print(" 3 para mostrar contacto")
	print(" 4 para mostrar lista de contactos")
def agregar_nom():
	print("ingrese nombre:--aqui hay un imput--")
	return
def agregar_ape():
	print("ingrese apellido:")
	return()
def agregar_tel():
	print("ingrese telefono:")
	return()
def agregar_mail():
	print("ingrese e-mail:")
	return()
def segundo_menu(opcion):
	system=Estructuras()
	exit=False
	if(opcion==1):
 		print("Lista doblemente enlazada:")
 		while(exit==False):
 			menu()
 			op=1
 			system.menu_list(op)
 			exit=system.menu_list(5)
 		return(False)
	if(opcion==2):
 		print("Arbol binario")
 		while(exit==False):
 			menu()
 			op=1
 			system.menu_abb(op)
 			exit=system.menu_abb(5)
 		return(False)
	if(opcion==3):
 		print("Arbol avl")
 		while(exit==False):
 			menu()
 			op=1
 			system.menu_abb(op)
 			exit=system.menu_abb(5)
 		return(False)
	if(opcion==4):
 		print("Arbol 2-3")
 		while(exit==False):
 			menu()
 			op=1
 			system.menu_abb(op)
 			exit=system.menu_abb(5)
 		return(False)
	if(opcion==5):
 		print("Hash")
 		while(exit==False):
 			menu()
 			op=1
 			system.menu_abb(op)
 			exit=system.menu_abb(5)
 		return(False)
	if(opcion==6):
		print("---saliendo al menu principal---")
		return(True)
def menu_principal():
	exit=False
	while(exit==False):
		print("Lista de contactos")
		print("¿que estructura desea ocupar para guardar sus contactos?")
		print("1- Lista doblemente enlazada")
		print("2- Arbol binario")
		print("3- Arbol avl")
		print("4- Arbol 2-3")
		print("5- Hash")
		exit=segundo_menu(2)
		exit=segundo_menu(6)
	return(print("!!!!!!finalizar programa!!!!!"))
menu_principal()

