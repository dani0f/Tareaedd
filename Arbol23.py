from faker import Faker
from listadoble import Lista_s
from listadoble import Nodo
from time import time
class Node:
	def __init__(self, data, par = None):
		#print ("Node __init__: " + str(data))
		self.data = list([data])
		self.parent = par
		self.child = list()
	def __str__(self):
		if self.parent:
			return str(self.parent.data) + ' : ' + str(self.data)
		return 'Root : ' + str(self.data)
	def __lt__(self, node):
		return self.data[0] < node.data[0]

	def _isLeaf(self):
		return len(self.child) == 0
	def _add(self, new_node):
		for child in new_node.child:
			child.parent = self
		self.data.extend(new_node.data)
		self.data.sort()
		self.child.extend(new_node.child)
		if len(self.child) > 1:
			self.child.sort()
		if len(self.data) > 2:
			self._split()

	# find correct node to insert new node into tree
	def _insert(self, new_node):
		if self._isLeaf():
			self._add(new_node)
		elif new_node.data[0] > self.data[-1]:
			self.child[-1]._insert(new_node)
		else:
			for i in range(0, len(self.data)):
				if new_node.data[0] < self.data[i]:
					self.child[i]._insert(new_node)
					break
	def _split(self):
		left_child = Node(self.data[0], self)
		right_child = Node(self.data[2], self)
		if self.child:
			self.child[0].parent = left_child
			self.child[1].parent = left_child
			self.child[2].parent = right_child
			self.child[3].parent = right_child
			left_child.child = [self.child[0], self.child[1]]
			right_child.child = [self.child[2], self.child[3]]

		self.child = [left_child]
		self.child.append(right_child)
		self.data = [self.data[1]]
		if self.parent:
			if self in self.parent.child:
				self.parent.child.remove(self)
			self.parent._add(self)
		else:
			left_child.parent = self
			right_child.parent = self
	def _find(self, item):
		if item in self.data:
			return item
		elif self._isLeaf():
			return False
		elif item > self.data[-1]:
			return self.child[-1]._find(item)
		else:
			for i in range(len(self.data)):
				if item < self.data[i]:
					return self.child[i]._find(item)

	def _remove(self, item):
		pass

	def _preorder(self):
		print (self)
		for child in self.child:
			child._preorder()
class Tree:
	def __init__(self):
		self.root = None
		self.list=Lista_s()
	def insert(self,nombre,apellido,telefono,mail):
		self.list._insertar(nombre,apellido,telefono,mail)
		if self.root is None:
			self.root = Node(apellido)
		else:
			self.root._insert(Node(apellido))
			while self.root.parent:
				self.root = self.root.parent
		return True
	def find(self, valor):
		return self.root._find(valor)
	def remove(self, valor):
		self.list.eliminar(valor)
		self.root.remove(valor)
	def preorder(self):
		print ('----Preorder----')
		self.root._preorder()
	def mostrar_todos(self):
		self.list.imprimir_todos()
	def mostrar_contacto(self,apellido):
		self.list.imprimir_contacto(apellido)
