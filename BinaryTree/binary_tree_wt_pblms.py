"""
1. Construct Binary Tree
2. Vertical Sum of Binary Tree

1    2    3     4    5
|    |    5     |    |
|    2    |     4    |
1    |   3 6    |    8
|    |    |     |    |
|    |    |     |    |

1 => 1
2 => 2
3 => 14
4 => 4
5 => 8

"""


class Node(object):
    def __init__(self, data, left=None, right=None):
        """
             Data
        LeftP   RightP

        :param data:
        :param left:
        :param right:
        """
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        pass

    def delete(self, data):
        pass


class BinaryTreeUtil(object):
    def in_order(self, root):
        """
        l => ro => ri
        :param root:
        :return:
        """
        if not root:
            return

        self.in_order(root.left)
        print(root.data),
        self.in_order(root.right)

    def pre_order(self, root):
        pass

    def post_order(self, root):
        pass

    def vertical_sum(self, root):

        if not root:
            return

        queue = [dict(node=root, hd=0)]
        vertical_sum_map = dict()

        while len(queue):
            item = queue.pop()

            if not item:
                break

            node = item['node']
            hd = item['hd']

            if hd not in vertical_sum_map:
                vertical_sum_map[hd] = 0

            vertical_sum_map[hd] += node.data

            if node.left:
                queue.append(dict(node=node.left, hd=hd-1))

            if node.right:
                queue.append(dict(node=node.right, hd=hd+1))

        return vertical_sum_map

    def max_width(self, root):
        pass


if __name__ == '__main__':
    # Driver

    root = Node(5)

    root.left = Node(2)
    root.right = Node(4)

    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right.left = Node(6)
    root.right.right = Node(8)

    bu = BinaryTreeUtil()

    # bu.in_order(root)
    print(bu.vertical_sum(root))


"""
Binary tree traversals
Ex:
        1
    2       3
4               6

1. Breadth first or Level order 
Ex: 1 2 3 4 6

2. Depth first
Ex: 4 2 1 3 6


Horizontal Distance (HD):
         0
         1
    2(-1)  3(+1)
 4(-2)          6(+2)
 
it: 0
EnQ => r

it: 1
DeQ => r
Q => [r.left, r.right]

it: 2
DeQ => r.left
Q => [r.right, r.left.left, r.left.right]

it: 3
DeQ => r.right
Q => [r.left.left, r.left.right, r.right.left, r.right.right]


Implement Q:
1. DS: Array
2. Element in an array is dict (HM) => {node: data, hd: distance}

Cal vertical sum:
vertical_sum_map = {hd: sum}

"""