from linkedlist import LinkedList


def main():
    data = [1, 2, 3, 4, 5]
    l = LinkedList()

    for each in data:
        l.insert(each)

    # l.print_list(l.head)
    # # l.reverse_using_iteration()
    # new_head = l.reverse(None, l.head)

    new_head = l.rotate(l.head, 18, 5)
    l.print_list(new_head)


main()
