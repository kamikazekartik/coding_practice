class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, l):
		self.head = None
		for item in l:
			self.push(item)

	def push(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while(current.next):
				current = current.next
			current.next = new_node

	def print_list(self):
		current = self.head
		output = ""
		while(current.next):
			output += str(current.data)
			output += " -> "
			current = current.next
		output += str(current.data)
		print output


	def reverse(self):
		prev = None
		current = self.head
		while(current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev


	# bloomberg question
	def odd_even(self):
		current = self.head
		odd_head = even_head = odd_p = even_p = None
		while(current):
			if(current.data%2 == 0):
				if(even_p is not None):
					even_p.next = current
					even_p = even_p.next
				else:
					even_head = current
					even_p = even_head
			else:
				if(odd_p is not None):
					odd_p.next = current
					odd_p = odd_p.next
				else:
					odd_head = current
					odd_p = odd_head
			
			current = current.next
		
		odd_p.next = None
		even_p.next = None
		# reverse evens
		prev = None
		current = even_head
		while(current):
			next = current.next
			current.next = prev
			prev = current
			current = next
		even_head = prev

		# combine the two
		odd_p.next = even_head
		self.head = odd_head



def recursive_reverse(current, prev=None):
	next = current.next
	current.next = prev

	if next is None:
		return current

	return recursive_reverse(next, current)



# testing code
l = LinkedList([1,2,3,4,5])
l.print_list()
l.reverse()
l.print_list()
l.head = recursive_reverse(l.head)
l.print_list()
l.odd_even()
l.print_list()

