class Stack:

    # constructor:

    def __init__(self):
        self.stack = []  # initialize an empty list to represent the stack

    def push(self, item):
        """ adds an item to the top of the stack """
        self.stack.append(item)

    def pop(self):
        """ removes and returns the item at the top of the stack """
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """ returns the item at the top of the stack without removing it """
        if self.is_empty():
            return None
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        """ checks if the stack is empty """
        return len(self.stack) == 0


if __name__ == "__main__":

    stack = Stack()

    # Push elements into the stack
    stack.push(5)
    stack.push(10)
    stack.push(15)

    # peek at the top element
    print("Top element:", stack.peek())

    # pop elements from the stack
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())  # Trying to pop from an empty stack

    # check if the stack is empty
    print("Is the stack empty?", stack.is_empty())
