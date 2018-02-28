class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, head, element):

        if not head:
            head = Node(element)
            return head

        temp = head

        while temp.next is not None:
            temp = temp.next

        temp.next = Node(element)

        return head

    def insert_after(self, after, element):
        pass

    def contains(self, head, key):
        if not head:
            raise Exception('LL is Empty')

        temp = head

        while temp is not None:

            if key in temp.data:
                return temp.data

            temp = temp.next

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

    def rotate(self, head, k, len):
        count = 1
        n = k % len

        current = head

        while count < n and current is not None:
            current = current.next
            count += 1

        if current is None:
            return

        kthnode = current

        while current.next is not None:
            current = current.next

        current.next = head
        head = kthnode.next
        kthnode.next = None

        return head