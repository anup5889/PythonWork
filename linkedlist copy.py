class Node:
#function to initialize the node object
	def __init__(self,data):
		self.data=data
		self.next=None

class Linkedlist:
	#intialize the Linkedlist object
	def __init__(self):
		self.head= None 

	#function to print the linkedlist
	def printList(self):
		temp= self.head
		while(temp):
			print temp.data,
			temp=temp.next

	#function to insert new node at the begining 
	def push(self, new_data):

		new_node=Node(new_data)

		#point the new_data.next to self.head
		new_data.next=self.head

		#assign the self.head to new_data
		self.head=new_data

		#self.head is just a pointer which points to the 
		#first Node in the linkedlist


	def insertAfter(self,previous_node, new_data): # passing the pointer "previous_node" and new_data
		if previous_node is None: 
			print "The Node should be present in the linkedList"
			return
		new_node=new_data(new_data)

		previous_node=new_node

		#make next of new_node as next of previous node
		new_node.next=previous_node.next
		previous_node.next=new_node

	def append(self, new_data):

		new_node=Node(new_data)
		last=self.head

		# list is empty add new_node as head

		if self.head is None:
			self.head=new_node

		while(temp.next):
			last.next
		last.next=new_node


	def deleteNode(self,key):

		#store head
		temp=self.head

		# if the key is present at the head
		if(temp is not None):
			if(temp.data==key):
				self.head=temp.next
				temp=None

		#if key is not present at head node 
		#iterate through the linkedlist
		while(temp is not None):
			if(temp.data==key):
				break
			prev=temp
			temp=temp.next

		#if key is not found
		if(temp is None):
			print "key is not found"
			return

		#unlink the node

		prev.next=temp.next
		temp=None






# creating the Linkedlist, its head and the other two nodes
llist=Linkedlist()
llist.head=Node(1)
second=Node(2)
third=Node(3)

#connecting the nodes 

llist.head.next=second
second.next=third

llist.printList()

