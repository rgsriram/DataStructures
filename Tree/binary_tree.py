class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    def verticalTraversal(self, root):

        if not root:
            return

        q = [dict(node=root, hd=0)]
        vertical_order = dict()

        while len(q) > 0:

            item = q.pop(0)

            if not item:
                break

            hd = item['hd']
            node = item['node']
            data = node.data

            if hd not in vertical_order:
                vertical_order[hd] = []

            vertical_order[hd].append(data)

            if node.left:
                q.append(dict(node=node.left, hd=hd-1))

            if node.right:
                q.append(dict(node=node.right, hd=hd+1))

        _dict = vertical_order

        keys = list(_dict.keys())
        keys.sort()
        result = []

        for k in keys:
            result.append(_dict[k])

        return result

    def invert_tree(self, root1, root2):
        if not root:
            return

        self.root

        


if __name__ == "__main__":
    n = Node(6)

    n.left = Node(3)
    n.right = Node(7)

    n.left.left = Node(2)
    n.left.right = Node(5)

    n.right.right = Node(9)

    print(Tree().verticalTraversal(n))
