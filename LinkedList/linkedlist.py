class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, element):

        if not self.head:
            self.head = Node(element)
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = Node(element)

    def insert_after(self, after, element):
        pass

    def reverse_using_iteration(self):
        prev = None
        current = self.head

        # 1 -> 2 -> 3 -> 4
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

    def reverse(self, previous, current):
        
        if current:
            next = current.next
            current.next = previous
            previous = current
            current = next
            return self.reverse(previous, current)
        
        return previous
            
    def print_list(self, head):

        while head is not None:
            print head.data,
            print '->',
            head = head.next

        print


def main():
    data = [1, 2, 3, 4, 5]
    l = LinkedList()

    for each in data:
        l.insert(each)

    l.print_list(l.head)
    # l.reverse_using_iteration()
    new_head = l.reverse(None, l.head)
    l.print_list(new_head)


main()