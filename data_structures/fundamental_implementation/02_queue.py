class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
        
    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front item:", queue.peek())
print("Size:", queue.size())

print("Dequeued item:", queue.dequeue())
print("Size after dequeue:", queue.size())      