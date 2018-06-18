class QueueUsingStack(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack1:
            print('Queue is empty')
            return

        self.stack2 = self.stack1[::-1]
        res = self.stack2.pop()
        self.stack1 = self.stack2[::-1]

        return res

    def head(self):
        return self.stack1[0] if self.stack1 else None


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):
    def __init__(self, capacity):
        self.front = None
        self.rear = None
        self.capacity = capacity

    def enQueue(self, data):

        if self.isFull():
            raise Exception('Queue is Full')

        if not self.rear:
            self.rear = Node(data)
            self.front = self.rear

        else:
            last = self.rear
            last.next = Node(data)
            self.rear = last.next

    def deQueue(self):
        if not self.front:
            raise Exception("Queue is Empty")

        first = self.front
        self.front = first.next

        return first.data

    def isEmpty(self):
        return bool(self.front or self.rear)

    def size(self, front, count=0):
        if not front:
            return count

        return self.size(front.next, count+1)

    def isFull(self):
        return self.size(self.front) >= self.capacity

    def printQueue(self, front):
        if not front:
            return

        print front.data
        self.printQueue(front.next)


def main():
    # q = QueueUsingStack()
    #
    # t = int(raw_input())
    #
    # for a0 in range(0, t):
    #     input = map(int, raw_input().split(' '))
    #
    #     if input[0] == 1:
    #         # EnQ
    #         q.enqueue(input[1])
    #
    #     elif input[0] == 2:
    #         # DeQ
    #         q.dequeue()
    #
    #     elif input[0] == 3:
    #         # print
    #         print(q.head())

    q = Queue(10)

    elements = [1, 2, 3, 4, 5, 8]

    for each in elements:
        q.enQueue(each)

    print 'Size: ', q.size(q.front)
    print 'Elements: '
    q.printQueue(q.front)

    print 'DeQueue: 1'
    print q.deQueue()
    print 'DeQueue: 2'
    print q.deQueue()
    # print 'DeQueue: 3'
    # print q.deQueue()
    # print 'DeQueue: 4'
    # print q.deQueue()
    # print 'DeQueue: 5'
    # print q.deQueue()
    # print 'DeQueue: 6'
    # print q.deQueue()
    # print 'DeQueue: 7'
    # print q.deQueue()

    print 'Elements: '
    q.printQueue(q.front)


main()
