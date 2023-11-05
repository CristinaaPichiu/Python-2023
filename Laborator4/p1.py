class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)

    print("Stack:", my_stack.stack)

    top_element = my_stack.pop()
    print("Popped element:", top_element)
    print("Stack after pop:", my_stack.stack)

    peek_element = my_stack.peek()
    print("Peeked element:", peek_element)

    print("Stack size:", my_stack.size())  
