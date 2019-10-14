class Stack(object):
    def __init__(self,limit= 10):
        self.stack = []
        self.limit = limit
    def push (self,data):
        if len(self.stack) >= self.limit:
            raise IndexError('超出栈容量的极限')
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('pop from an empty stack')
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def size(self):
        return len(self.stack)
    
