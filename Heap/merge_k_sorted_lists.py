import heapq


# def add_to_heap(h, i, it):
#
#     try:
#         heapq.heappush(h, (next(it), i))
#
#     except StopIteration:
#         pass
#
#
# def mergeK(*lists):
#     its = map(iter, lists)
#     h = []
#
#     for i, it in enumerate(its):
#         add_to_heap(h, i, it)
#
#     while h:
#         v, i = heapq.heappop(h)
#         add_to_heap(h, i, its[i])
#         yield v
#
# for x in mergeK([1, 3, 5], [2, 4, 6], [7, 8, 9], [10]):
#     print x


class Node(object):
    def __init__(self, index, arr, value):
        self.index = index
        self.arr = arr
        self.value = value

    def __cmp__(self, other):
        return cmp(self.value, other.value)


def add_to_heap(h, node):
    heapq.heappush(h, node)


def merge_lists(*lists):
    h = []
    size = 0

    for i in range(len(lists)):
        size += len(lists[i])
        # h.append(Node(0, i, lists[i][0]))
        add_to_heap(h, Node(0, i, lists[i][0]))

    results = [0] * size
    i = 0

    while len(h):
        node = heapq.heappop(h)
        results[i] = node.value
        new_index = node.index + 1

        if new_index < len(lists[node.arr]):
            add_to_heap(h, Node(new_index, node.arr, lists[node.arr][new_index]))

        i += 1
    print results

merge_lists([1, 3, 5],[7, 8, 9], [2, 4, 6], [10])


