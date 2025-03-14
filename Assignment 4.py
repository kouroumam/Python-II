from collections import deque

class DequeQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        item = self.queue.popleft()
        return item

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

if __name__ == "__main__":

    queue = DequeQueue()

    print(f"Is the queue empty? {queue.is_empty()}")

    queue.enqueue("apple")
    queue.enqueue("banana")
    queue.enqueue("cherry")

    print(f"Queue size: {queue.size()}")

    queue.dequeue()
    queue.dequeue()

    print(f"Queue size: {queue.size()}")

    print(f"Is the queue empty? {queue.is_empty()}")

    queue.dequeue()

    print(f"Is the queue empty? {queue.is_empty()}")

    try:
        queue.dequeue()
    except IndexError as e:
        print(e)
