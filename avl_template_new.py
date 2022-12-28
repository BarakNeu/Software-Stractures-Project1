#username - omrikaplan
#id1      - 319089256
#name1    - Omri Kaplan
#id2      - 209422054
#name2    - Barak Neuberger

import random



"""A class represnting a node in an AVL tree"""
import math
import random
import sys
class AVLNode(object):
	"""Constructor, you are allowed to add more fields.
	@type value: str
	@param value: data of your node
	"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.size = 1
		self.height = 0  # Balance factor
		self.is_real_node = True

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

	def getLeft(self):#works in 0(1)
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):#works in 0(1)
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):#works in 0(1)
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):#works in 0(1)
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):#works in 0(1)
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):#works in 0(1)
		self.left = node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):#works in 0(1)
		self.right = node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):#works in 0(1)
		self.parent = node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):#works in 0(1)
		self.value= value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):#works in 0(1)
		self.height = h
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self): #works in 0(1)
		return self.is_real_node
def fixSizeUpwards(node):  #works in O(log(n))
	while node.parent is not None:
		node.parent.size = node.parent.right.size + node.parent.left.size + 1
		node = node.parent

def CreateVarNode(): #works in O(1)
	emptyNode = AVLNode(None)
	emptyNode.left = None
	emptyNode.right = None
	emptyNode.parent = None
	emptyNode.size = 0
	emptyNode.height = -1  # Balance factor
	emptyNode.is_real_node = False
	return emptyNode



"""
A class implementing the ADT list, using an AVL tree.
"""
def mergesort(lst): # works in O(nlog(n)) from intro to cs
	n = len(lst)
	if n <= 1:
		return lst
	else:
		return merge(mergesort(lst[0:n//2]), mergesort(lst[n//2:n]))
def merge(A, B): #from intro to cs, works in O(n+m) where n and m are the length of A and B
	n = len(A)
	m = len(B)
	C = [None for i in range(n+m)]
	a = 0; b = 0; c = 0
	while a < n  and b < m:
		if A[a] < B[b]:
			C[c] = A[a]
			a += 1
		else:
			C[c] = B[b]
			b += 1
		c += 1
	C[c:] = A[a:] + B[b:]
	return C
class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		self.min = None
		# add your fields here


	def successor(self, node):  # finding a node's successor O(log(n))
		if node.right.is_real_node is False:
			parent = node.parent
			while node == parent.right and parent is not None:
				node = parent
				parent = node.parent
		else:
			while node.left.is_real_node and node.left is not None:
				node = node.left
		return node

	# noinspection DuplicatedCode
	def predeccessor(self, node): #same as successor, just swtiching left with right and vise versa. O(log(n))
		if node.left.is_real_node is False:
			parent = node.parent
			while node == parent.left and parent is not None:
				node = parent
				parent = node.parent
		else:
			while node.right.is_real_node and node.right is not None:
				node = node.right
		return node

	def rank(self, node):  # finding a node's rank O(log(n))
		r = node.left.size + 1
		x = node
		while x.parent is not None:
			if x == x.parent.right:
				r += x.parent.left.size + 1
			x = x.parent
		return r
	"""returns whether the list is empty
	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

	def empty(self):
		if self.size == 0:
			return True
		return False
	def tree_select(self, k):
		def tree_select_rec(node, k):
			r = node.left.size + 1
			if k == r:
				return node
			elif k < r and node.left.is_real_node:
				return tree_select_rec(node.left, k)
			elif node.right.is_real_node:
				return tree_select_rec(node.right, k - r)
			else:
				return
		return tree_select_rec(self.root, k)


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		if i < 0 or i > self.size or self.size == 0:
			return None
		return self.tree_select(i+1).value


	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		cnt = 0 #number of balancing fixes
		toInsert = AVLNode(val)
		toInsert.right = CreateVarNode()
		toInsert.left = CreateVarNode()
		toInsert.right.parent = toInsert
		toInsert.left.parent = toInsert
		if self.root is None:
			self.root = toInsert
			self.min = toInsert
			self.root.size += 1
			self.size += 1
			return 0
		if i == 0: #inserting to the start of the list
			toInsert.parent = self.min
			self.min.left = toInsert
			self.min = toInsert
		elif i == self.size: #inserting to the end of the list
			n = self.root
			while n.right.isRealNode():
				n = n.right
			n.setRight(toInsert)
			toInsert.setParent(n)
		else: #finding rank i+1 and inserting as left child if that position is open
			currNode = self.tree_select(i+1)
			if not currNode.left.isRealNode():
				currNode.left = toInsert
				toInsert.setParent(currNode)
			else: #finding i+1's predescessor and inserting as max to it's left sub-tree
				currNode = self.predeccessor(currNode)
				currNode.setRight(toInsert)
				toInsert.parent = currNode
		cnt += self.balanceUp(toInsert.parent)
		fixSizeUpwards(toInsert)
		self.size += 1
		return cnt
	def leftRotate(self, z): #+1 to fixing actions O(1)
		y = z.right
		T2 = y.left
		# Perform rotation
		y.left = z
		z.right = T2
		# organize parents
		y.parent = z.parent
		z.parent = y
		T2.parent = z
		if y.parent is not None:
			y.parent.right = y
		# Update heights and sizes
		z.height = 1 + max(z.left.getHeight(), z.right.getHeight())
		y.height = 1 + max(y.left.getHeight(), y.right.getHeight())
		z.size = 1 + z.left.size + z.right.size
		y.size = 1 + y.left.size + y.right.size
		return 1
	def rightRotate(self, z): ##+1 to fixing actions
		y = z.left
		T3 = y.right
		# Perform rotation
		y.right = z
		z.left = T3
		# origzine parents
		y.parent = z.parent
		z.parent = y
		T3.parent = z
		if y.parent is not None:
			y.parent.left = y
		# Update heights and sizes
		z.height = 1 + max(z.left.getHeight(), z.right.getHeight())
		y.height = 1 + max(y.left.getHeight(), y.right.getHeight())
		# Return the number of corrections done
		return 1

	def leftRightRotate(self, z): #+2 to fixing actions
		self.leftRotate(z.left)
		self.rightRotate(z)
		# Return the number of corrections done
		return 2

	def rightLeftRotate(self, z): ##+2 to fixing actions
		self.rightRotate(z.right)
		self.leftRotate(z)
		# Return the number of corrections done
		return 2

	def balanceUp(self, n):
		cnt = 0
		n.height += 1
		while n.getParent() is not None:
			n = n.getParent()
			n.height = 1 + max(n.left.height, n.right.height)
			BF = n.left.height - n.right.height
			if BF == -2 and n.right.left.height - n.right.right.height == -1:
				cnt += self.leftRotate(n)
				continue
			elif BF == -2 and n.right.left.height - n.right.right.height == 1:
				cnt += self.rightLeftRotate(n)
				continue
			elif BF == 2 and n.left.left.height - n.left.right.height == -1:
				cnt += self.leftRightRotate(n)
				continue
			elif BF == 2 and n.left.left.height - n.left.right.height == 1:
				cnt += self.rightRotate(n)
				continue
			else:
				continue
		self.root = n
		return cnt

	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		cnt = 0
		currNode = self.tree_select(i+1) #getting to the node
		needToBalFrom = currNode.parent
		self.delNode(currNode)
		cnt += self.balanceUp(needToBalFrom)
		return cnt
	def delNode(self, currNode): ##returns the node from wise the balanceUp needs to accure
		if not currNode.right.isRealNode() and not currNode.left.isRealNode():
			if currNode.parent.right == currNode:
				currNode.parent.right = CreateVarNode()
			else:
				currNode.parent.left = CreateVarNode()
		elif currNode.right.isRealNode() and currNode.left.isRealNode():
			suc = self.successor(currNode)
			## recursive with successor
			## asked Omri to try
			self.delNode(suc)
		elif not currNode.right.isRealNode():
			if currNode.parent.right == currNode:
				currNode.parent.right = currNode.left
			else:
				currNode.parent.left = currNode.left
		elif not currNode.left.isRealNode():
			if currNode.parent.right == currNode:
				currNode.parent.right = currNode.right
			else:
				currNode.parent.left = currNode.right
		return


	"""returns the value of the first item in the list
	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self): #works in O(1)
		return self.min

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self): #works in O(log(n))
		if self.size == 0:
			return None
		node = self.root
		while node.right.is_real_node:
			node = node.right
		return node

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self): # works like inorder walk, O(n) whereas n is the length of the list
		array = []
		if self.size == 0:
			return []
		def listToArray_rec(node, array):
			if node.is_real_node is False:
				return
			listToArray_rec(node.left, array)
			array.append(node.value)
			listToArray_rec(node.right, array)
		return listToArray_rec(self.root, array)
	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self): #works in O(1)
		return self.size

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self): #works in O(n) because of the listToArray
		tree_array = self.listToArray()
		sorted_tree = AVLTreeList
		sorted_tree_array = mergesort(tree_array)
		for i in range(len(tree_array)):
			sorted_tree.insert(i, sorted_tree_array[i])
		return sorted_tree

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self): #works in O(n) because of the listToArray
		permed_tree = AVLTreeList
		tree_array = self.listToArray()
		rand_locations = random.sample(range(0, self.size - 1), self.size)
		for i in range(len(tree_array)):
			permed_tree.insert(i, tree_array[rand_locations[i]])
		return permed_tree

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst): #works in O(log(|n-m|)) whereas n is the size of self and m is the size of lst
		#follow the algorithm from the class
		# waiting for barak's "fix from here upward" function


		return abs(self.root.height - lst.root.height)

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val): #works in O(nlog(n)) proof from recitation 
		node = self.min
		if node.value == val:
			return self.rank(node)
		while self.successor(node).value != val:
			node = self.successor(node)
		if node == self.min: # if after the loop it's still the min then val is not in the list
			return -1
		return self.rank(node)
	"""returns the root of the tree representing the list
	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self): #works in 0(1)
		return self.root
	def append(self, val):
		self.insert(self.length(), val)

