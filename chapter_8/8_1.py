"""
Design a stack that includes a max operation, in addition to push and 
pop.  The max method should return the maximum value in the stack.
"""

#It's pretty trivial to implement a stack.  We can either track the int,
#or the index of the element that is the max stack.

class StackWithMax:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def pop(self):    
        if self.is_empty:
            raise Exception('underflow')
        else:
            return self.items.pop()

    def get_max(self):
        return max(self.items)