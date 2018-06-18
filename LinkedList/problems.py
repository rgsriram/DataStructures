from linkedlist import LinkedList


def merge_sorted_ll1(h1, h2):

    if not h2:
        return h1

    if not h1:
        return h2

    if h1.data > h2.data:
        h2.next = merge_sorted_ll1(h1, h2.next)
        return h2

    else:
        h1.next = merge_sorted_ll1(h1.next, h2)
        return h1


def merge_sorted_ll(h1, h2, h=None):

    if h1 and h2:
        if not h:
            if h1.data > h2.data:
                h = h2
                h2 = h2.next

            else:
                h = h1
                h1 = h1.next

        else:
            if h1.data > h2.data:
                h.next = h2
                h2 = h2.next

            else:
                h.next = h1
                h1 = h1.next

            h = h.next

    elif h1:
        h.next = h1

    elif h2:
        h.next = h2

    else:
        return h

    merge_sorted_ll(h1, h2, h)

    return h


def merge_sorted_ll2(h1, h2, h):

    if not h1:
        return h2

    if not h2:
        return h1

    if h1.data > h2.data:
        h = merge_sorted_ll2(h1, h2.next)
        return h2

    else:
        h1.next = merge_sorted_ll2(h1.next, h2)
        return h1


def main():
    data = [1, 8, 8, 29,30]
    l = LinkedList()
    # h1 = None
    # h2 = None

    # for each in data:
    #     h1 = l1.insert(h1, each)
    #
    # data = [2, 9]
    # l2 = LinkedList()
    #
    # for each in data:
    #     h2 = l2.insert(h2, each)
    #
    # h = merge_sorted_ll1(h1, h2)
    #
    # l1.print_list(h)

    head = None

    for each in data:
        head = l.insert(head, each)

    l.print_list(head)
    # new_head = l.reverse_m_n(head, 2, 4)
    # print new_head.next.next.data
    # new_head = l.reverse(None, l.head)

    # new_head = l.rotate(l.head, 18, 5)
    # print head.data
    new_head = l.remove_duplicates(head)
    l.print_list(new_head)

    # print l.is_palindrome(head)

main()
