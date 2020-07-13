"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def empty_stack(self):
        return len(self.storage) == 0

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)
        print('Pushed item: ', value)

    def pop(self):
        if self.empty_stack():
            return 'Stack is empty'

        self.storage.pop()


stack = Stack()

stack.push(4)
stack.push(2)
stack.push(6)
stack.push(9)
stack.push(2)
print( stack.storage)

print('stack after delete an element')
stack.pop()
print(stack.storage)
