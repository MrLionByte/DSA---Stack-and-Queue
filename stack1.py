# STACK

class Stack_simple:
    def __init__(self):
        self.stack = []

    def push(self, elemnt):
        self.stack.append(elemnt)
    
    def pop(self):
        if self.isEmpty():
            return 'Empty stack'
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Empty stack'
        return self.stack[-1]
    
    def isEmpty(self):
        return not bool(self.stack)
    
    def size(self):
        return len(self.stack)

stack_build = Stack_simple()
stack_build.push(2)
stack_build.push(3)
stack_build.push(5)
print('STACK' , stack_build.stack)

print('POP' , stack_build.pop())
print('Peek' , stack_build.peek())
print('Is Empty' , stack_build.isEmpty())
print('Size' , stack_build.size())

# Stack Using LinkedList
print('LINKED LIST')
print('    <<>>     ')
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def print_linkedlist(self):
        current = self.head
        while True:
            if current is None:
                break
            print(current.data, end='->')
            current = current.next
        print(None)

    def pop(self):
        if self.isEmpty():
            return 'Stack Empty'
        popped_node = self.head 
        self.head = self.head.next
        self.size -= 1
        return popped_node.data
    
    def peek(self):
        if self.isEmpty():
            return 'Empty Stack'
        return self.head.data

    def isEmpty(self):
        return self.size == 0
    
    def stacksize(self):
        return self.size

stack_obj = Stack()
arr = ['A','B','C','D','E','F','G']
for i in arr:
    stack_obj.push(i)


stack_obj.print_linkedlist()
print(stack_obj.stacksize())
print(stack_obj.isEmpty())
print(stack_obj.pop())
print(stack_obj.peek())
print(stack_obj.stacksize())



# Reverse Stack
print('STACK REVERSE')
print('             >><<            ')

class Stack_rev:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        popped = self.stack.pop()
        return popped

    def print_stack(self):
        print(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def stack_reverse(self):
        aux_stack = Stack_rev()
        while not self.is_empty():
            aux_stack.push(self.pop())
        self.stack = aux_stack.stack

stack_reverse = Stack_rev()
for i in arr:
    stack_reverse.push(i)
stack_reverse.print_stack()
stack_reverse.stack_reverse()
stack_reverse.print_stack()


# Reverse Stack
print('STACK RECURSION REVERSE')
print('             >>  <<            ')

class Stack_rev_rec:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        popped = self.stack.pop()
        return popped

    def print_stack(self):
        print(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def inset_at_bottom(self, data):
        if self.is_empty():
            self.push(data)
        else:
            temp = self.pop()
            print('DATA', data)
            self.inset_at_bottom(data)
            print('insert bottom temp', temp)
            self.push(temp)
            print(self.stack, 'In recuirsuon')
        
    def stack_reverse(self):
        if not self.is_empty():
            temp = self.pop()
            print('Stack Reverse', temp)
            self.stack_reverse()
            print('Stack Reversed afterrr', temp)
            self.inset_at_bottom(temp)


stack_reverse = Stack_rev_rec()
for i in arr:
    stack_reverse.push(i)
stack_reverse.print_stack()
stack_reverse.stack_reverse()
stack_reverse.print_stack()

