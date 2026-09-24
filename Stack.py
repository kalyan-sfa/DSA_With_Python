#Stack using List
'''stack = []

#push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

#pop
stack.pop()
print("After pop: ", stack)

#Peek
print("Top element: ", stack[-1])'''

#Full stack Implementation
'''print("Implemantation of stack")
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stacck) == 0

    def display(self):
        print(self.stack)


#Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()
s.pop()
s.display()

print("Popped: ", pop())
print("Tpo: ", peek())
print(s.is_empty())
'''

#Stack using Linked List
'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            print("Stack Underflow")
            return

        temp = self.top
        self.top = self.top.next
        return temp.data

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("NULL")


s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped: ", s.pop())
s.display()'''

#Parenthesis Checking
'''def is_balanced(expr):
    stack = []

    for char in expr:
        if char in "({[":    
            stack.append(char)
        else:
            if not stack:
                return False

            top = stack.pop()

            if( (char == ")" and top != "(") or
                (char == "}" and top != "{") or
                (char == "]" and top != "[")):
                return False

    return len(stack) == 0

print(is_balanced("{[()]}"))'''


#Stack with overflow
class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, data):
        if len(self.stack) == self.capacity:
            print("Stack Overflow")
            return
        self.stack.append(data)

    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return
        return self.stack.pop()

    def display(self):
        print(self.stack)

s = Stack(3)
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.push(40)

s.display()