class Node(object):
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class QueueUsingDLL(object):
    def __init__(self, capacity):
        self.front = None
        self.rear = None
        self.capacity = capacity
        self.size = 0

    def isFull(self):
        return self.size >= self.capacity

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, data):

        if self.isFull():
            raise Exception('Queue is full')

        if not self.front:
            self.front = Node(data)
            self.rear = self.front

        else:
            front = self.front
            node = Node(data, prev=None, next=front)
            front.prev = node
            self.front = node

        self.size += 1

        return self.front

    def deQueue(self):

        if self.isEmpty():
            raise Exception('Queue is empty')

        rear = self.rear
        rear.prev.next = None
        self.rear = rear.prev
        self.size -= 1

        return rear

    def printQueue(self):

        current = self.front

        while current is not None:
            print(current.data)
            current = current.next


class LRUCache(object):
    def __init__(self):
        self.pages = dict()
        self.capacity = 3
        self.queue = QueueUsingDLL(self.capacity)

    def refer(self, page_num):

        if self.queue.isFull():
            node = self.queue.deQueue()
            # if node.data in self.pages:
            del self.pages[node.data]

        if page_num in self.pages:
            node = self.pages[page_num]
            node.prev = node.next
            node.next.prev = node.prev
            del self.pages[page_num]

        node = self.queue.enQueue(page_num)
        self.pages[page_num] = node


if __name__ == '__main__':
    lru = LRUCache()

    lru.refer(1)
    lru.refer(2)
    lru.refer(3)

    print('Queue')
    lru.queue.printQueue()

    print '\n'
    lru.refer(4)
    lru.refer(1)
    lru.refer(5)

    print('Queue')
    lru.queue.printQueue()



