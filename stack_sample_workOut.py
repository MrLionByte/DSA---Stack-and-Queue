# Create a stack using array do following operation (push, pop, peek , is empty, seize)
# Create a stack using linked list do following operation (push, pop, peek , is empty, seize)
# Create  a stack and reverse a string
# Create  a stack using array and reverse it using recursion

class Stack:
    def __init__(self) -> None:
        self.stack= []
    
    def build_stack(self, val):
        self.stack.append(val)
    
    def insert_bottom(self, arr):
        arr = arr[::-1]
        
    
    def reverse_rec(self):
        if len(self.stack) < 1:
            return

        popped = self.stack.pop()
        self.reverse_rec()
        self.build_stack(popped) 
    
    def display(self):
        print(self.stack)

st = Stack()
for i in range(0,10):   
    st.build_stack(i)
st.reverse_rec()
st.display()