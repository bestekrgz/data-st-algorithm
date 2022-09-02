# Stack Operations
# Push
# The operation to insert elements in a stack is called push.
# When we push the book on a stack, we put the book on the previous top element which means that the new book becomes the top element.
# This is what we mean when we use the push operation, we push elements onto a stack.
# We insert elements onto a stack and the last element to be pushed is the new top of the stack.

# Pop
# There is another operation that we can perform on the stack, popping. Popping is when we take the top book of the stack and put it down.
# This means that the top element, the last to be inserted, is removed when we perform the pop operation.


# Peek

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items

# #
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# my_stack.push(3)
# my_stack.pop()
# print(my_stack.is_empty())
# print(my_stack.peek())