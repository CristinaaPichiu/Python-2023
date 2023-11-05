class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    my_queue = Queue()

    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)

    print("Queue:", my_queue.queue)

    front_element = my_queue.pop()
    print("Popped element:", front_element)
    print("Queue after pop:", my_queue.queue)

    peek_element = my_queue.peek()
    print("Front element:", peek_element)

    print("Queue size:", my_queue.size())
