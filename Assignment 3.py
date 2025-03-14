

class Queue:
    def __init__(self):
        self.queue = []


    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue error, its empty")
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":

    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    print("Queue includes the following: ", queue.queue)
    print("Size of the queue is: ", queue.size())

    print("Dequeue item: ", queue.dequeue())
    print("Queue includes the following: ", queue.queue)

    print("Is the queue empty? ", queue.empty())
