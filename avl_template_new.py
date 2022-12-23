<<<<<<< Updated upstream
#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  
=======
#username - omrikaplan
#id1      - 319089256
#name1    - Omri Kaplan
#id2      - 209422054
#name2    - Barak Neuberger
>>>>>>> Stashed changes



"""A class represnting a node in an AVL tree"""

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
			self.height = 0 # Balance factor
			self.is_ver_node = False

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""
	def getLeft(self):
		return self.left


	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""
	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def getParent(self):
		return self.parent

	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""
	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def setLeft(self, node):
		self.left = node
		return None

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def setRight(self, node):
		self.right = node
		return None

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def setParent(self, node):
		self.parent = node
		return None

	"""sets value

	@type value: str
	@param value: data
	"""
	def setValue(self, value):
		self.value= value
		return None

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""
	def setHeight(self, h):
		self.height = h
		return None

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.is_ver_node

	def CreateVarNode (self):
		emptyNode = AVLNode(None)
		emptyNode.left = None
		emptyNode.right = None
		emptyNode.parent = None
		emptyNode.size = 0
		emptyNode.height = -1  # Balance factor
		emptyNode.is_ver_node = True
		return emptyNode


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.size = 0
		self.root = None
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		return None


	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
<<<<<<< Updated upstream
		return None
=======
		return tree_select(self.root, i+1).value
>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
		return -1
=======
		cnt = 0 ##number of balancing fixes
		myNode = AVLNode(val)
		if i == 0:
			self.min = myNode
		if seach(val) != -1:
			return -1
		if this.root == None:
			this.root = myNode
			self.min = myNode
			return 0
		if i == self.root.size:
			###inserting to the end of the list
			n = self.root
			while n.right.isRealNode():
				n = n.right
			myNode.setRight(n.right)
			myNode.setLeft(CreateVarNode())
			n.setRight(myNode)
			myNode.setParent(n)
			## need to run balancing here
			cnt += balanceUp(self, myNode)
		else:
			###finding rank i+1 and inserting as left child if that position is open
			currNode = tree_select(self,i+1)
			if not currnode.left.isRealNode():
				myNode.setleft(currNode.left)
				myNode.setRight(CreateVarNode())
				n.setLeft(myNode)
				myNode.setParent(currNode)
				## need to run balancing here
				cnt += balanceUp(self, myNode)
			else:
				###finding i+1's predescessor and inserting as max to it's left sub-tree
				n = currNode.left
				while n.right.isRealNode():
					n = n.right
				myNode.setRight(n.right)
				myNode.setLeft(CreateVarNode())
				n.setRight(myNode)
				myNode.setParent(n)
				##need to run balancing here
				cnt += balanceUp(self, myNode)

		return cnt




	def leftRotate(self, z): ##+1 to fixing actions
		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2
		# origzine parents
		y.parent = z.parent
		z.parent = y
		T2.parent = z

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

		return 1

	def rightRotate(self, z): ##+1 to fixing actions
		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3
		#origzine parents
		y.parent = z.parent
		z.parent = y
		T3.parent = z

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))

		# Return the number of corrections done
		return 1

	def leftRightRotate(self, z): ##+2 to fixing actions
		leftRotate(self, z.left)
		rightRotate(self, z)
		# Return the number of corrections done
		return 2

	def rightLeftRotate(self, z): ##+2 to fixing actions
		rightRotate(self, z.right)
		leftRotate(self, z)
		# Return the number of corrections done
		return 2

	def balanceUp(self, n):
		cnt = 0
		while n.parent != None
			n = getParent(n)
			BF = n.left.height - n.right.height
			if BF == -2 and n.right.left.height - n.right.right.height == -1:
				cnt += rotateLeft(self, n)
			elif BF == -2 and n.right.left.height - n.right.right.height == 1:
				cnt += rotateRightLeft(self, n)
			elif BF == 2 and n.left.left.height - n.left.right.height == -1:
				cnt += rotateLeftRight(self, n)
			elif BF == 2 and n.left.left.height - n.left.right.height == 1:
				cnt += rotateRight(self, n)
			else: continue
		return cnt


>>>>>>> Stashed changes


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		cnt = 0
		currNode = tree_select(self,i+1)
		needToBalFrom = currNode.parent
		delNode(self, currNode)
		cnt += balanceUp(self, needToBalFrom)
		return cnt

	def delNode(self, currNode): ##returns the node from wise the balanceUp needs to accure
		if not currNode.right.isRealNode() and not currNode.left.isRealNode():
			if currNode.parent.right == currNode:
				currNode.prent.right = CreateVarNode()
			else:
				currNode.parent.left = CreateVarNode()
		elif currNode.right.isRealNode() and currNode.left.isRealNode():
			suc = successor(self, currNode)

			## recursive with successor
			## asked Omri to try
			delNode(self, suc)


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
	def first(self):
		return None

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		return None

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""
	def listToArray(self):
		return None

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return None

	"""sort the info values of the list

	@rtype: list
	@returns: an AVLTreeList where the values are sorted by the info of the original list.
	"""
	def sort(self):
		return None

	"""permute the info values of the list 

	@rtype: list
	@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
	"""
	def permutation(self):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		return None






