class Queue:

    # constructor:

    def __init__(self):
        self.queue = []

    def push(self, item):
        """ adds an item to the end of the queue """
        self.queue.append(item)

    def pop(self):
        """ removes and returns the item from the front of the queue """
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def peek(self):
        """ returns the item from the front of the queue without removing it """
        if self.is_empty():
            return None
        return self.queue[0]

    def is_empty(self):
        """ checks if the queue is empty """
        return len(self.queue) == 0


if __name__ == "__main__":
    my_queue = Queue()

    my_queue.push(5)
    my_queue.push(10)
    my_queue.push(15)

    print("First element:", my_queue.peek())

    print("Removed:", my_queue.pop())
    print("Removed:", my_queue.pop())
    print("Removed:", my_queue.pop())
    print("Removed:", my_queue.pop())  # Trying to pop from an empty queue

    print("Is the queue empty?", my_queue.is_empty())
