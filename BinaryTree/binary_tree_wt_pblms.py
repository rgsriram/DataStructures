import sys
import json
from collections import OrderedDict

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

_sum = 0

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

    def __init__(self):
        self.sum = 0
        self.paths = []
        self.prev = None

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

    def _is_leaf(self, node):

        if not node:
            return False

        return not (node.left or node.right)

    def is_sum_tree(self, root):

        if not root or self._is_leaf(root):
            return 1

        if self.is_sum_tree(root.left) and self.is_sum_tree(root.right):

            if root.left is None:
                left_sum = 0

            elif self._is_leaf(root.left):
                left_sum = root.left.data

            else:
                left_sum = 2 * root.left.data

            if root.right is None:
                right_sum = 0

            elif self._is_leaf(root.right):
                right_sum = root.right.data

            else:
                right_sum = 2 * root.right.data

            return root.data == left_sum + right_sum

        return False

    def findkthlargest(self, root, k, n, d=None):
        if not root:
            return

        self.findkthlargest(root.right, k, n, d)

        if n == k:
            d = root.data
            print 'HERE'
            return d

        n += 1

        return self.findkthlargest(root.left, k, n)

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
                vertical_sum_map[hd] = []

            vertical_sum_map[hd].append(node.data)

            if node.left:
                queue.append(dict(node=node.left, hd=hd-1))

            if node.right:
                queue.append(dict(node=node.right, hd=hd+1))

        return vertical_sum_map

    def max_width(self, root):

        if not root:
            return 0

        queue = [root]
        width = 0

        while len(queue):
            width = max(len(queue), width)

            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return width

    def sum_of_leaf_nodes(self, root):

        queue = [root]
        sum = 0

        while len(queue):

            node = queue.pop(0)

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

            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if node.right or node.left:
                height += 1

        return height

    def is_symmetric(self, root):

        queue = [root]

        while len(queue):

            node = queue.pop(0)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            if (node.left and not node.right) or (node.right and not node.left):
                return 0

            if node.left.data != node.right.data:
                return 0

        return 1

    def max_min_height(self, root):

        if not root:
            return 0, 0

        queue = [{'node': root, 'depth': 1}]

        max_depth = 0
        min_depth = sys.maxint

        while len(queue):

            item = queue.pop(0)

            node = item['node']
            depth = item['depth']

            if not node.left and not node.right:
                min_depth = min(min_depth, depth)
                max_depth = max(max_depth, depth)

            if node.left:
                queue.append({'node': node.left, 'depth': depth+1})

            if node.right:
                queue.append({'node': node.right, 'depth': depth + 1})

        return min_depth, max_depth

    def min_height(self, root):

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.right:
            return self.min_height(root.left) + 1

        if not root.left:
            return self.min_height(root.right) + 1

        return min(self.min_height(root.left), self.min_height(root.right)) + 1

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

    def _in_order(self, root, nodes):
        """
        l => ro => ri
        :param root:
        :return:
        """
        if not root:
            return

        self._in_order(root.left, nodes)
        nodes.append(root.data)
        self._in_order(root.right, nodes)

        return nodes

    def pairs_voilates_BST(self, root):
        nodes = self._in_order(root, [])
        swaps = 0

        for i in range(1, len(nodes)):
            value = nodes[i]
            hole = i

            while hole > 0 and nodes[hole-1] > value:
                nodes[hole] = nodes[hole-1]
                swaps += 1
                hole -= 1

            nodes[hole] = value

        print swaps

    def lca(self, root, x, y):

        if not root:
            return None

        if root.data in [x, y]:
            return root

        left = self.lca(root.left, x, y)
        right = self.lca(root.right, x, y)

        if left and right:
            return root

        if not left and not right:
            return

        return left if left else right.data

    def _sum_root_to_leaf(self, root, nodes, nums):
        if not root:
            return

        if root.left is None and root.right is None:
            nums.append(int(''.join(map(str, nodes + [root.data]))))
            return nums

        if root.left:
            self._sum_root_to_leaf(root.left, nodes + [root.data], nums)

        if root.right:
            self._sum_root_to_leaf(root.right, nodes + [root.data], nums)

        return nums

    def sum_root_to_leaf(self, root, nodes):
        nums = self._sum_root_to_leaf(root, nodes, [])

        int_res = sum(nums) % 1003

        print int_res % 1003

    def is_balanced(self, root):
        if not root:
            return 1

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        return bool(abs(lheight-rheight) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right))

    def height(self, root):

        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def zig_zag_traversal(self, root):
        s1 = [root]
        s2 = []

        while len(s1) or len(s2):

            res = []
            while len(s1):
                node = s1.pop()
                res.append(node.data)

                if node.right:
                    s2.append(node.right)

                if node.left:
                    s2.append(node.left)

            print res
            res = []
            while len(s2):
                node = s2.pop()
                res.append(node.data)

                if node.left:
                    s1.append(node.left)

                if node.right:
                    s1.append(node.right)

            print res

    def lca2(self, A, B, C):
        paths_1 = self.ancestors(A, B, [])
        paths_2 = self.ancestors(A, C, [])

        i = 0
        j = 0
        ilen = len(paths_1)
        jlen = len(paths_2)

        while (i < ilen) and (j < jlen):

            if paths_1[i] != paths_2[j]:
                break

            i += 1
            j += 1

        lca = paths_1[i - 1] if i > 0 else paths_2[j - 1]

        return lca

    def ancestors(self, root, target, nodes=[]):
        if not root:
            return False

        nodes.append(root.data)

        if root.data == target:
            return nodes

        if self.ancestors(root.left, target, nodes) or self.ancestors(root.right, target, nodes):
            return nodes

        nodes.pop()
        return False

    def left_view(self, root):

        if not root:
            return

        queue = [root]
        print root.data,

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left:
                print node.left.data,
            elif node.right:
                print node.right.data,

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def right_view(self, root):

        if not root:
            return

        queue = [root]
        print root.data,

        while len(queue) > 0:
            node = queue.pop(0)

            if node.right:
                print node.right.data,
            elif node.left:
                print node.left.data,

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

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
                print node.data,

            if node.left:
                queue.append(dict(node=node.left, hd=hd - 1))

            if node.right:
                queue.append(dict(node=node.right, hd=hd + 1))

    def bottom_view(self, root):

        if not root:
            return

        queue = [dict(node=root, hd=0)]
        nodes = {}

        while len(queue) > 0:
            element = queue.pop(0)
            node = element['node']
            hd = element['hd']

            nodes[hd] = node.data
            print node.data,

            if node.left:
                queue.append(dict(node=node.left, hd=hd - 1))

            if node.right:
                queue.append(dict(node=node.right, hd=hd + 1))

    def flatten(self, root):

        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None

        self.prev = root

        return self.prev

    def flattenDLL(self, root):

        if not root:
            return

        self.flattenDLL(root.right)

        root.right = self.prev

        if self.prev:
            self.prev.left = root

        self.prev = root

        self.flattenDLL(root.left)

        return self.prev

    def findMaxPerfectTree(self, root, max_size=0):
        if not root:
            return max_size

        if not root.left or not root.right:
            return 0

        ls = self.findMaxPerfectTree(root.left, max_size+1)
        rs = self.findMaxPerfectTree(root.right, max_size+1)

        return 1 + max(ls, rs)

    def serialize(self, root):

        if not root:
            return []

        queue = [root]
        result = [root.data]

        while len(queue) > 0:
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
                result.append(node.left.data)
            else:
                result.append(None)

            if node.right:
                queue.append(node.right)
                result.append(node.right.data)
            else:
                result.append(None)

        for i in range(len(result)-1, 0, -1):
            if result[i]:
                break
            result.pop(i)

        return result

    def _deserailize(self, root, element, i=0):

        pass

    def deserialize(self, string):
        data = json.loads(string)

        root = Node(data[0])

        for i in range(1, len(data)):



#
# class DLL(object):
#     def __init__(self, data, prev, next):
#         self.data = data
#         self.prev = prev
#         self.next = next


def identical_tree(root1, root2):

    if not all([root1, root2]):
        return True

    if (root1 and not root2) or (root2 and not root1):
        return False

    if root1.data != root2.data:
        return False

    return identical_tree(root1.left, root2.left) and identical_tree(root1.right, root2.right)

if __name__ == '__main__':
    # Driver

    # Sum Tree
    # root = Node(26)
    # root.left = Node(10)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(6)
    # root.right.right = Node(3)

    # root = Node(50)
    #
    # root.left = Node(30)
    #
    # root.left.left = Node(20)
    # root.left.right = Node(25)
    #
    # # root.left.left.left = Node(100)
    #
    # root.right = Node(60)
    #
    # root.right.left = Node(10)
    # root.right.right = Node(40)

    # root = Node(30)
    #
    # root.left = Node(20)
    # root.right = Node(50)
    #
    # root.right.left = Node(40)
    # root.right.right = Node(60)
    #
    # root.right.right.right = Node(70)



    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.right.left = Node(4)
    root.right.right = Node(5)


    # elements = [1, 3, 4, 6, 8]
    bu = BinaryTreeUtil()
    print(bu.deserialize(json.dumps(bu.serialize(root))))

    # for each in elements:
    #     bu.insert(root, each)

    # bu.in_order(root)
    # print '\n'
    # print bu.findkthlargest(root, 0, 0)
    # h = bu.flattenDLL(root)
    #
    # while h is not None:
    #     print h.data,
    #
    #     if h.left:
    #         print h.left.data,
    #
    #     h = h.right
    #     print

    # while h:
    #     print h.data,
    #     h = h.left

    # print bu.sum_of_leaf_nodes(root)
    # bu.delete(root, 5)
    # h = bu.max_height(root)
    # print
    # print h
    # bu.print_all_path(root, [])
    # bu.sum_root_to_leaf(root, [])

    # print bu.is_balanced(root)
    # bu.zig_zag_traversal(root)

    # print bu.max_width(root)
    # print bu.max_min_height(root)

    # bu.left_view(root)
    # print
    # bu.right_view(root)
    # print
    # bu.top_view(root)
    # print bu.lca2(root, 10, 40)
    # print bu.ancestors(root, 30)
    # print bu.ancestors(root, 40)
    # print bu.paths
    # bu.print_ancestors(root, 10)
    # print 'Size: ', bu.size(root)
    # print 'Size: ', bu.hasPathSum(root, 16)
    # print bu.is_sum_tree(root)
    # bu.pairs_voilates_BST(root)
    # bu.in_order(root)
    # bu.in_order(root)
    # print(bu.vertical_sum(root))
    # print bu.lca(root, 30, 25).data
    # print(bu.findMaxPerfectTree(root))


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