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


class BT(object):
    def sorted_arr_to_BST(self, arr, st, end):
        if not len(arr):
            return

        if st > end:
            return

        m = (st + end) // 2

        node = Node(arr[m])
        print 'Left: ', st, end, m
        node.left = self.sorted_arr_to_BST(arr, st, m-1)
        print 'Right: ', st, end, m
        node.right = self.sorted_arr_to_BST(arr, m+1, end)

        return node

    def preoder(self, root):
        if not root:
            return

        print(root.data),
        self.preoder(root.left)
        self.preoder(root.right)

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

arr = [1, 2, 3, 4, 5]
root = BT().sorted_arr_to_BST(arr, 0, len(arr)-1)
BT().in_order(root)