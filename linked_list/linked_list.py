from node import Node


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = Node(data)
        node.set_next_node(self.head)
        self.head = node

    def size(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.get_next_node()
        return size

    def search(self, data):

        current = self.head
        found = False

        while current:
            if current.get_data() == data:
                found = True
                break
            current = current.get_next_node()

        if found:
            return current

        return None

    def delete(self, data):

        current = self.head
        found = False

        while current.get_next_node():
            if current.get_next_node().get_data() == data:
                found = True
                break
            current = current.get_next_node()

        if found:
            current.set_next_node(current.get_next_node().get_next_node())

        return found

    def print_list(self):
        current = self.head
        found = False

        while current:
            print "%s -> " % current.get_data(),
            current = current.get_next_node()

        print "\n"

        if found:
            return current


if __name__ == '__main__':

    linked_list = LinkedList()
    exit = False

    while not exit:
        option = raw_input("Enter options to continue\n1.Insert\n2.Search\n3.Delete\n4.Print\n5.Exit\n")

        if str(option) == "1":
            data = raw_input("Enter element to insert: ")
            linked_list.insert(data)
        elif str(option) == "2":
            data = raw_input("Enter element to select: ")
            node = linked_list.search(data)
            print "Found the node: %s" % node.get_data()
        elif str(option) == "3":
            data = raw_input("Enter element to delete: ")
            success = linked_list.delete(data)
            print "Deleted Successfully." if success else "Deletion failed"
        elif str(option) == "4":
            linked_list.print_list()
        else:
            exit = True

        print "\n"

