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


class BinaryTreeUtil(object):
    def insert(self, root, data):

        if root.data < data:

            if root.right is None:
                root.right = Node(data)

            else:
                self.insert(root.right, data)
        else:

            if root.left is None:
                root.left = Node(data)

            else:
                self.insert(root.left, data)

    def max_val_node(self, root):
        current = root

        while current.right is not None:
            current = current.right

        return current

    def delete(self, root, data):
        if root is None:
            return

        elif root.data < data:
            root.right = self.delete(root.right, data)

        elif root.data > data:
            root.left = self.delete(root.left, data)

        else:

            if root.left is None:
                temp = root.right
                return temp

            elif root.right is None:
                temp = root.left
                return temp

            else:
                _max_val_node = self.max_val_node(root.left)
                root.data = _max_val_node.data
                self.delete(root.left, _max_val_node.data)

        return root

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

    def findkthlargest(self, root, k, n):
        if not root:
            return

        self.findkthlargest(root.right, k, n)

        if n == k:
            print "Lar: %s" % root.data
            return

        n += 1

        self.findkthlargest(root.left, k, n)

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

    def sum_of_leaf_nodes(self, root):

        queue = [root]
        sum = 0

        while len(queue):

            node = queue.pop()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if not node.left and not node.right:
                sum += node.data

        return sum

    def max_height(self, root):

        queue = [root]
        height = 0

        while len(queue):

            node = queue.pop()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if node.right or node.left:
                height += 1

        return height

    def print_all_path(self, root, nodes):
        if not root:
            return

        if root.left is None and root.right is None:
            print ' -> '.join(map(str, nodes + [root.data]))
            return

        if root.left:
            self.print_all_path(root.left, nodes + [root.data])

        if root.right:
            self.print_all_path(root.right, nodes + [root.data])

    def print_ancestors(self, root, k):
        if not root:
            return

        if root.data == k:
            return True

        if self.print_ancestors(root.left, k) or self.print_ancestors(root.right, k):
            print root.data
            return True

    def size(self, root, size=0):

        if not root:
            return 0

        return self.size(root.left, size+1) + 1 + self.size(root.right, size+1)

    def hasPathSum(self, root, sum):

        subsum = sum - root.data

        if not root:
            return sum

        if root.left:
            s = self.hasPathSum(root.left, subsum)

        if root.right:
            s = self.hasPathSum(root.left, subsum)

        return s

if __name__ == '__main__':
    # Driver

    root = Node(5)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.left.right = Node(10)
    root.left.right = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(9)

    # elements = [1, 3, 4, 6, 8]
    bu = BinaryTreeUtil()

    # for each in elements:
    #     bu.insert(root, each)

    # bu.in_order(root)
    print '\n'
    # bu.findkthlargest(root, 0, 0)
    # print bu.sum_of_leaf_nodes(root)
    # bu.delete(root, 5)
    # h = bu.max_height(root)
    # print
    # print h
    # bu.print_all_path(root, [])
    # bu.print_ancestors(root, 10)
    # print 'Size: ', bu.size(root)
    print 'Size: ', bu.hasPathSum(root, 16)
    # bu.in_order(root)
    # print(bu.vertical_sum(root))


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