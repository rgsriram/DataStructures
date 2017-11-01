from min_heap import MinHeap


def build_min_heap(elements):
	min_heap = MinHeap()

	i = len(elements) // 2
	min_heap.current_size = len(elements)
	min_heap.heap_list = [0] + elements[:]

	while i > 0:
		min_heap.perc_down(i)
		i -= 1

	print min_heap.heap_list[1:]


if __name__ == '__main__':
	build_min_heap([0, 9, 5, 6, 2, 3])

