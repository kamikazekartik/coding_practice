class randNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.rand = None

def clone(head):
	current = head
	current_clone = None
	while(current):
		new_node = randNode(current.data)
		if current_clone:
			current_clone.next = new_node
			current_clone = current_clone.next
		else:
			current_clone = new_node

		next = current.next
		current_clone.rand = current
		current.next = current_clone
		current = next

	# fix the random pointers
	head_clone = head.next
	current = head_clone
	while(current):
		current.rand = current.rand.rand.next
		current = current.next

	return head_clone


def print_list(head):
	current = head
	while(current):
		data = current.data
		next = current.next.data if current.next else -1
		rand = current.rand.data
		print data, "->", next, "-->", rand
		current = current.next

# testing code
n1 = randNode(1)
n2 = randNode(2)
n3 = randNode(3)
n4 = randNode(4)
n5 = randNode(5)
n6 = randNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

n1.rand = n3
n2.rand = n5
n3.rand = n6
n4.rand = n6
n5.rand = n3
n6.rand = n1

print_list(n1)
l = clone(n1)
print_list(l)