from Arbol2_3 import Node
from Arbol2_3 import Tree
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
		if(opcion==1):
			nombre,apellido,telefono,mail=agregar_datos()
			self.list._insertar(nombre,apellido,telefono,mail)
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.list.eliminar(ape)
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.list.imprimir_contacto(ape)
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
	def menu_2_3(self,opcion):
		if(opcion==1):#agregar contacto
			print("---agregar contacto---------------")
			nombre,apellido,telefono,mail=agregar_datos()
			self.arbol_23.insertar(nombre,apellido,telefono,mail)
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.arbol_23.remove(ape)
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.arbol_23.mostrar_contacto(ape)
			print("----------------------------------")
			return(False)
		if(opcion==4):
			print("---Mostrando Lista de contactos---")
			self.arbol_23.mostrar_todos()
			print("----------------------------------")
			return(False)
		if(opcion==5):
			print("---exit---------------------------")
			print("saliendo de Arbol 2-3")
			print("----------------------------------")
			return(True)
	def menu_abb(self,opcion):
		if(opcion==1):
			print("---agregar contacto---------------")
			nombre,apellido,telefono,mail=agregar_datos()
			self.abb.add(nombre,apellido,telefono,mail)
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.abb.delete(ape)
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.abb.print_contact(ape)
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
			nombre,apellido,telefono,mail=agregar_datos()
			self.avl.add(nombre,apellido,telefono,mail)
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.avl.delete(ape)
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.avl.print_contact(ape)
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
		if(opcion==1):
			print("---agregar contacto---------------")
			nombre,apellido,telefono,mail=agregar_datos()
			self.hash.put(nombre,apellido,telefono,mail)
			print("----------------------------------")
			return(False)
		if(opcion==2):
			print("---eliminar contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.hash.H_eliminar(ape)
			print("----------------------------------")
			return(False)
		if(opcion==3):
			print("---imprimir contacto--------------")
			print("ingrese apellido:")
			ape=input()
			self.hash.H_imprimir_contacto(ape)
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
	print(" 5 para salir")
def agregar_datos():
	print("ingrese nombre:")
	nom=input()
	print("ingrese apellido:")
	ape=input()
	print("ingrese telefono:")
	tel=input()
	print("ingrese e-mail:")
	mail=input()
	return(nom,ape,tel,mail)
def segundo_menu(opcion):
	system=Estructuras()
	exit=False
	if(opcion==1):
		print("Lista doblemente enlazada:")
		while(exit==False):
 			menu()
 			opcion=int(input())
 			exit=system.menu_list(opcion)
	if(opcion==2):
		print("Arbol binario")
		while(exit==False):
 			menu()
 			opcion=int(input())
 			exit=system.menu_abb(opcion)
	if(opcion==3):
		print("Arbol avl")
		while(exit==False):
 			menu()
 			opcion=int(input())
 			exit=system.menu_abb(opcion)
	if(opcion==4):
 		print("Arbol 2-3")
 		while(exit==False):
 			menu()
 			opcion=int(input())
 			exit=system.menu_abb(opcion)
	if(opcion==5):
		print("Hash")
		while(exit==False):
 			menu()
 			opcion=int(input())
 			exit=system.menu_hash(opcion)
	if(opcion==6):
		print("---saliendo al menu principal---")
		return(True)
	return(False)
#------------------------------------------------------------------------
exit=False
while(exit==False):
	print("--------------------------------------------------------")
	print("Lista de contactos")
	print("--------------------------------------------------------")
	print("¿que estructura desea ocupar para guardar sus contactos?")
	print("1- Lista doblemente enlazada")
	print("2- Arbol binario")
	print("3- Arbol avl")
	print("4- Arbol 2-3")
	print("5- Hash")
	print("6- salir")
	opcion=int(input())
	print(":::::::::opcion::::::::::",opcion)
	exit=segundo_menu(opcion)
	print("!!!!!!finalizar programa!!!!!")