# QUE with array

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self ,val):
        self.data.append(val)
    
    def dequeue(self):
        if self.isEmprty():
            return 'Emprty Queue'
        popped = self.data.pop(0)
        return popped
    
    def peek(self):
        if self.isEmprty():
            return 'Emprty Queue'
        return self.data[0]
    
    def isEmprty(self):
        return not self.data
    
    def size(self):
        return len(self.data)

queue = Queue()
for i in range(2,10):
    queue.enqueue(i)
print(queue.dequeue())
print(queue.isEmprty())
print(queue.peek())
print(queue.size())

#### Queue 
print('        >>>  <<<        ')
print( 'Linked List Queue' )
print('        >>>  <<<        ')
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class Queue_linkedList:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.rear = self.front = new_node
            self.length += 1
            return

        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def print_linkedlist(self):
        current = self.front
        while current:
            print(current.data, end='->')
            current = current.next
        print(None)

    def dequeue(self):
        if self.isEmpty():
            return 'Empty Queue'
        deq_pop = self.front
        self.front = self.front.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return deq_pop.data

    def isEmpty(self):
        return self.length == 0
    
    def queue_length(self):
        return self.length
    
    def display(self):
        return self.front.data
    
    def middle_element(self):
        i = 0
        middle_node = self.front
        print('length', self.length//2)
        while i < self.length//2:
            middle_node=middle_node.next
            i += 1
        return middle_node.data

linked_queue = Queue_linkedList()
for i in range(2,6):
     linked_queue.enqueue(i)

print(linked_queue.isEmpty())
print(linked_queue.queue_length())
print(linked_queue.dequeue())
linked_queue.print_linkedlist()
print(linked_queue.display())
print(linked_queue.middle_element())

# Reverse Queue using recursion
print('                     ')
print('         >>>  <<<            ')


class Queue_rec:
    def __init__(self) -> None:
        self.queue = []
    
    def print_queue(self):
        print(self.queue)

    def enqueue(self, data):
        self.queue.append(data)

    def reverse_queue(self):
        if len(self.queue) == 0:
            return
        popped = self.queue.pop(0)
        print('popped', popped)
        self.reverse_queue()
        print('After recurse', popped)
        self.queue.append(popped)
        


queue = Queue_rec()
for i in range(2,8):
    queue.enqueue(i)
queue.enqueue(8)
queue.reverse_queue()
queue.print_queue()
        
