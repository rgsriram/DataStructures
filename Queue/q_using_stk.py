
class QueueUsingStack(object):

	def __init__(self):
		self.stack1 = []
		self.stack2 = []


	def enqueue(self, element):
		self.stack1.append(element)


	def dequeue(self):
		if not self.stack1:
			print('Queue is empty')
			return

		self.stack2 = self.stack1[::-1]
		res = self.stack2.pop()
		self.stack1 = self.stack2[::-1]

		return res

	def head(self):
		return self.stack1[0] if self.stack1 else None

def main():
	q = QueueUsingStack()

	t = int(raw_input())

	for a0 in range(0, t):
		input = map(int, raw_input().split(' '))

		if input[0] == 1:
			# EnQ
			q.enqueue(input[1])

		elif input[0] == 2:
			# DeQ
			q.dequeue()

		elif input[0] == 3:
			# print
			print(q.head())

main()