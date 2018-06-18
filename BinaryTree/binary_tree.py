class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class View(object):
    def left_view(self, root):
        pass

    def top_view(self, root):

        if not root:
            return

        queue = [dict(node=root, hd=0)]
        nodes = {}

        while len(queue) > 0:
            element = queue.pop(0)
            node = element['node']
            hd = element['hd']

            if hd not in nodes:
                nodes[hd] = node.data

            if node.left:
                queue.append(dict(node=node.left, hd=hd - 1))

            if node.right:
                queue.append(dict(node=node.right, hd=hd + 1))

        print(' '.join(map(str, nodes.values())))


def main():
    """
			  1
		2	 		3	
	4		5	6		7
	"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    v = View()
    v.top_view(root)


main()




