class Node:


	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

	def insert(self,data):
		if self.data == data:
			return False # node already exists
		elif self.data > data:
			if self.left != None:
				return self.left.insert(data)
			else: 
				self.left = Node(data) # if there is no left child
				return True
		else: 
			if self.right != None: # if the data is graeter than the elemtn insert it into the rght child
				return self.right.insert(data)
			else:
				self.right = Node(data) # if there is no left child
				return True
	def node_exists(self,value):
		if self.data == value:
			return True
		if self.right != None:
			return self.right.node_exists(value)
		if self.left != None:
		    return self.left.node_exists(value)

		return False



	def preorder(self):
		if self != None:
			print str(self.data),
		if self.left != None:
			self.left.preorder()
		if self.right != None:
			self.right.preorder()

	def inorder(self):	
		if self != None:
			if self.left != None:
				self.left.inorder()
			print str(self.data),		
			if self.right != None:
				self.right.inorder()

	def postorder(self):
		if self != None:
			if self.left != None:
				self.left.postorder()
			if self.right != None:
				self.right.postorder()
			print str(self.data),
			
 
	def rotate_right(self):
		aux = self.left  			# set temporary pointer aux to grandparent's left child
		self.left = aux.right 		# set grandparents left child's pointer, pointing to aux's right child
		aux.right = self 			# set aux right child = grandparent 
		return aux					# use aux inplace of grandparent

	def rotate_left(self):
		aux = self.right            # set temporary pointer aux to grandparent's right child
		self.right = aux.left       # set grandparent's right child's pointer, pointing to aux's left child
		aux.left = self             # set aux left child = grandparent
		return aux         			# use aux inplace of grandparent

	def rotate_right_left(self):
		self.right = self.right.rotate_right()				# rotate parent to the right
		return self.rotate_left()							# rotate grandparent to the left and return


	def rotate_left_right(self):
		self.left = self.left.rotate_left()						# rotate parent to the left
		return self.rotate_right()								# rotate grandparent to the right and return

	def remove(self,value):
		if self.node_exists(value) == True:
			parent = None
			while self and self.data != value:      # find the desired element
				parent = self
				if value < self.data:
				 	self = self.left
				if value > self.data:
				 	self = self.right

				
									
		 	if self.right == None and self.left == None: # leaf node removal: Just set the parent's pointer to NULL
		 		if value < parent.data:
		 			parent.left = None
		 		else:
		 			parent.right = None

		 		return True

		 	if self.right == None and self.left != None: # node with left child removal
		 		if value < parent.data:
		 			parent.left = self.left
		 		else:
		 			parent.right = self.left
		 		return True

		 	if self.right != None and self.left == None: # node with right child removal
		 		if value < parent.data:
		 			parent.left = self.right
		 		else:
		 			parent.right = self.right
		 		return True
		 	

		 	if self.right != None and self.left != None: # Node with both of his children removal
		 		auxparent = self
		 		aux = self.right
		 		while aux.left:
		 			auxparent = aux
		 			aux = aux.left

		 		self.data = aux.data
		 		if aux.right:
		 			if auxparent.data > aux.data:
		 				auxparent.left = aux.right
		 			if auxparent.data < aux.data:
		 				auxparent.right = aux.right
		 		else:
		 			if aux.data < auxparent.data:
		 				auxparent.left = None
		 			else:
		 				auxparent.right = None

			
			
									
		else:
		 	return False		


class BinarySearchTree:

	def __init__(self):
		self.root = None

	def insert(self,value):
		if self.root == None:
			self.root = Node(value)
		else:
			 self.root.insert(value)

	def preorder(self):
		print 'Pre Order:',
		self.root.preorder()
		print ' '

	def postorder(self):
		print 'Post Order:',
		self.root.postorder()
		print ' '

	def inorder(self):
		print 'In Order:',
		self.root.inorder()	
		print ' '

	def rotate_right(self):
		print('Rotating Right On Grandparent... Done!')
		return self.root.rotate_right()


	def rotate_left(self):
		print('Rotating Left On Grandparent... Done!')
		return self.root.rotate_left()

	def rotate_left_right(self):
		print('Rotating parent node to the left and grandparent node to the right...')
		return self.root.rotate_left_right()       # chain here traversal function to see tree after rotation

	def rotate_right_left(self):
		print('Rotating parent node to the right and grandparent node to the left...')
		return self.root.rotate_right_left()       # chain here traversal function to see tree after rotation

	def node_exists(self,value):
		if self.root.node_exists(value) == True:
			print('The Node with the value %d exists in your Binary Search Tree!' % value)
		else:
			print('No such node found!')	


	def remove(self,value):
		if self.root.remove(value) == True:
			print('Removal was Successfull!')
		else:
			print('No such node exists!')





bst = BinarySearchTree()
bst.insert(45)
bst.insert(50)
bst.insert(55)
bst.remove(45)











# Printing binary tree in ASCII, later
my = [1,2,3,4,5,6]
t = 50
def print_tri(my):

	if len(my) == 6:	
		for x in range(0,len(my)):
				if x == 0:
					print(' '*t  + str(my[x]))
					print(' '*(t - 1) + '/' + ' ' + '\\')
					print(' '*(t - 2) + '/' + '   ' + '\\')
					print(' '*(t - 3) + '/' + '     ' + '\\')
					print(' '*(t - 4) + '/' + '       ' + '\\')
				if x == 1:
				 	print ' '*(t-5)+str(my[x]) + ' '*9 + str(my[x + 1]),
				 	print ' '      # line break
				 	print ' '*(t - 6)+ '/'+ ' ' + '\\' + ' '*7 + '/'+ ' ' + '\\'
				 	print ' '*(t - 7)+ '/'+ '   ' + '\\' + ' '*5 + '/'+ '   ' + '\\'
				if x == 2:
					if my[x + 1] != None:
						print ' '*(t-8)+str(my[x + 1]),
					if my[x + 2] != None:
						print '  ' + str(my[x + 2]),
					if my[x + 3] != None:
						print '  ' + str(my[x + 3])
			




# RED BLACK TRREE RULES
'''
 	1. Root is always black.
 	2. Every node is either red or black.
 	3. New node is always red.
 	4. No consecutive 2 red nodes.
 	5. Every path must have the same number of black nodes
 	6. Nulls are black
'''
# Rebalance
	# Black aunt ---> rotate
	# red aunt ---> color-flip
# After rotation 
'''
	black
	/   \
  RED    RED
'''
# After color-flip
'''

	Red
   /   \
Black  Black

'''