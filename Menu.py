
def menu():
	print(" 1 para agregar contacto nuevo")
	print(" 2 para eliminar contactos")
	print(" 3 para mostrar contacto")
	print(" 4 para mostrar lista de contactos")
def agregar_nom():
	print("ingrese nombre:")
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
print("Lista de contactos")
print("¿que estructura desea ocupar para guardar sus contactos?")
print("1- Lista doblemente enlazada")
print("2- Arbol binario")
print("3- Arbol avl")
print("4- Arbol 2-3")
print("5- Hash")
opcion=1
exit=False
if(opcion==1):
	print("Lista doblemente enlazada")
	while(exit==False):
		menu()
		menu_opcion=1
		if(menu_opcion==1):
			#agrego en lista enlazada
			nom=agregar_nom()
			ape=agregar_ape()
			tel=agregar_tel()
			mail=agregar_mail()
			#list.agregar(nom,ape,tel,mail)
		if(menu_opcion==5):
			exit=True
if(opcion==2):
	print("Arbol binario")
if(opcion==3):
	print("Arbol avl")
	menu()
if(opcion==4):
	print("Arbol 2-3")
	menu()
if(opcion==5):
	print("Hash")
	menu()
if(opcion==6):
	print("---saliendo---")
	menu()