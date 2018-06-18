MIN = float('-inf')
MAX = float('inf')

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class ConstructBST(object):

    def __init__(self):
        self.index = 0

    def build_from_inorder(self, _inorder, st, end):

        if not len(_inorder):
            return

        if st > end:
            return

        m = (st + end) // 2

        root = Node(_inorder[m])
        root.left = self.build_from_inorder(_inorder, st, m-1)
        root.right = self.build_from_inorder(_inorder, m+1, end)

        return root

    def build_from_preorder(self, preorder, key, mini, maxi, size):
        if self.index > size:
            return

        root = None

        if mini < key < maxi:
            root = Node(key)
            self.index += 1

            if self.index < size:
                root.left = self.build_from_preorder(preorder, preorder[self.index], mini, key, size)
                root.right = self.build_from_preorder(preorder, preorder[self.index], key, maxi, size)

        return root

    def build_from_postorder(self, postorder, key, mini, maxi):

        if self.index < 0:
            return

        root = None

        if mini < key < maxi:
            root = Node(key)
            self.index -= 1

            if self.index > 0:
                root.right = self.build_from_postorder(postorder, postorder[self.index], key, maxi)
                root.left = self.build_from_postorder(postorder, postorder[self.index], mini, key)

        return root


def inorder(root):
    if not root:
        return

    inorder(root.left)
    print root.data,
    inorder(root.right)


def construct_post_order():
    postorder = [1, 7, 5, 50, 40, 10]
    bst = ConstructBST()
    bst.index = len(postorder) - 1
    root = bst.build_from_postorder(postorder, postorder[bst.index], MIN, MAX)
    inorder(root)


def construct_pre_order():
    preorder = [10, 5, 1, 7, 40, 50]
    bst = ConstructBST()
    bst.index = 0
    root = bst.build_from_preorder(preorder, preorder[bst.index], MIN, MAX, len(preorder))
    inorder(root)


def construct_inorder():
    _inorder = [1, 5, 7, 10, 40, 50]
    bst = ConstructBST()
    root = bst.build_from_inorder(_inorder, 0, len(_inorder) -1)
    inorder(root)

# construct_pre_order()
construct_inorder()