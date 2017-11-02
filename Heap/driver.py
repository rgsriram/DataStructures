from heaps import MinHeap, MaxHeap
import heapq


def build_min_heap(elements):
    min_heap = MinHeap()

    i = len(elements) // 2
    min_heap.current_size = len(elements)
    min_heap.heap_list = [0] + elements[:]

    while i > 0:
        min_heap.perc_down(i)
        i -= 1

    print min_heap.heap_list[1:]


def build_max_heap(elements):
    max_heap = MaxHeap()

    i = len(elements) // 2
    max_heap.current_size = len(elements)
    max_heap.heap_list = [0] + elements[:]

    while i > 0:
        max_heap.perc_down(i)
        i -= 1

    print max_heap.heap_list[1:]


if __name__ == '__main__':
    li = [0, 9, 5, 6, 2, 3]

    build_min_heap(li)
    build_max_heap(li)

    # heapq.heapify(li)
    heapq._heapify_max(li)
    print li
