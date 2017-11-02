class MinHeap(object):
	def __init__(self):
		self.heap_list = []
		self.current_size = 0


	def perc_up(self, i):
		"""
		Move the leaf node is lesser than root, move it up.
		"""
		while (i // 2) > 0:
			if self.heap_list[i] < self.heap_list[i//2]:
				self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]

			i //= 2



	def insert(self, element):
		self.heap_list.append(element)
		self.current_size += 1
		self._perc_up(self.current_size)


	def perc_down(self, i):
		"""
		Swap the root node, till acheiving heap property
		"""
		while (i*2) <= self.current_size:
			min_pos = self._min(i)

			if self.heap_list[i] > self.heap_list[min_pos]:
				self.heap_list[i], self.heap_list[min_pos] = self.heap_list[min_pos], self.heap_list[i]

			i = min_pos			


	def _min(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2

		else:
			if self.heap_list[i*2] < self.heap_list[i*2 + 1]:
				return i * 2

			else:
				return i * 2 + 1


	def del_min(self):
		element = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size -= 1
		self.heap_list.pop()
		self._perc_down(1)

		return element


class MaxHeap(object):
	def __init__(self):
		self.heap_list = []
		self.current_size = 0


	def perc_up(self, i):
		"""
		Move the leaf node is lesser than root, move it up.
		"""
		while (i // 2) > 0:
			if self.heap_list[i] < self.heap_list[i//2]:
				self.heap_list[i], self.heap_list[i//2] = self.heap_list[i//2], self.heap_list[i]

			i //= 2



	def insert(self, element):
		self.heap_list.append(element)
		self.current_size += 1
		self._perc_up(self.current_size)


	def perc_down(self, i):
		"""
		Swap the root node, till acheiving heap property
		"""
		while (i*2) <= self.current_size:
			max_pos = self._max(i)

			if self.heap_list[i] < self.heap_list[max_pos]:
				self.heap_list[i], self.heap_list[max_pos] = self.heap_list[max_pos], self.heap_list[i]

			i = max_pos			


	def _max(self, i):
		if i * 2 + 1 > self.current_size:
			return i * 2

		else:
			if self.heap_list[i*2] > self.heap_list[i*2 + 1]:
				return i * 2

			else:
				return i * 2 + 1


	def del_max(self):
		element = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size -= 1
		self.heap_list.pop()
		self._perc_down(1)

		return element

