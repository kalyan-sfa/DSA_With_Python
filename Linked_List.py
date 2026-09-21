#TRAVARSAL (Display Linked List)
print("Traversal in Linked List")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Create list manually
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

#Traversal
temp = head
while temp:
    print(temp.data, end = " -> ")
    temp = temp.next
print("NULL")

#Insertion at the beginning
print("\n")
print("Insertion at beginning")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Existing list
head = Node(20)
head.next = Node(30)

#Inserting at beginning
new_node = Node(10) # [10|none]
new_node.next = head
head = new_node

# Print
temp = head
while temp:
    print(temp.data, end = " -> ")
    temp = temp.next
print("NULL")

#Insertion at end
print("\n")
print("Insertion at End")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Existiong list 
head = Node(10)
head.next = Node(20)

#Inserting the data at end
new_node = Node(30)

temp = head
while temp.next:
    temp = temp.next

temp.next = new_node

# Print
temp = head
while temp:
    print(temp.data, end = " -> ")
    temp = temp.next

print("NULL")

#Insertion at a particular position
print("\n")
print("Insertion at a Position")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Existing list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)


# Position and data to insert
position = 2
new_node = Node(25)


# Inserting the data at position
if position == 0:
    new_node.next = head
    head = new_node

else:
    temp = head

    # Move to the node before the position
    for i in range(position - 1):
        temp = temp.next

    new_node.next = temp.next
    temp.next = new_node


# Print
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")

#Deletion (by value)
print("\nDeleting a Node")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Existing list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

tem = head
val = 20
print(f"List before deleting {val}")
while tem:
    print(tem.data, end = " -> ")
    tem = tem.next
print("NULL")

#Delete 20
key = 20
temp = head
prev = None

while temp and temp.data != key:
    prev = temp
    temp = temp.next

if temp == head:
    head = head.next
elif temp:
    prev.next = temp.next

#Print
print(f"List after deleting {key}")
temp = head
while temp:
    print(temp.data, end = " -> ")
    temp = temp.next
print("NULL")

#Doubly Linked List
print("\nDoubly Linked List")
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = DNode(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " <-> ")
            temp = temp.next
        print("NULL")

#Usage
dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.display()

#Circular Linked List
print("\nCircular Linked List")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def display(self):
        if not self.head:
            return

        temp = self.head
        while True:
            print(temp.data, end = " -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)

cll.display()
