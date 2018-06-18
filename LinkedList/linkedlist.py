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

    def remove_duplicates(self, head):

        if not head:
            return head

        if head.next and head.data == head.next.data:
            head.next = head.next.next

        else:
            head = head.next

        self.remove_duplicates(head)

        print head.data if head else None

        return head

    def reverse_m_n(self, head, m, n):
        nh = head
        prev = head

        for i in range(m-2):
            prev = prev.next

        current = prev.next

        for i in range(m, n):
            next = current.next
            current.next = next.next
            next.next = prev.next
            prev.next = next

        return nh

    def get_mid(self, head):
        count = 0
        current = head
        mid = head

        while current is not None:

            if count & 1:
                mid = mid.next

            count += 1
            current = current.next

        return count, mid

    def is_palindrome(self, head):
        count, mid = self.get_mid(head)

        if count % 2:
            second = mid.next

        else:
            second = mid

        current = head
        second_reversed = self.reverse(None, second)

        while current is not None:

            if current.data != second_reversed.data:
                return False

            if hex(id(current.next)) == hex(id(mid)):
                break

            current = current.next
            second_reversed = second_reversed.next

        return True