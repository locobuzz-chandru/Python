class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add_node(self, value):
        obj = TreeNode(value)
        _node = self.root

        def fun(node, val):
            if node is not None:
                if val < node.value:
                    if node.left is None:
                        node.left = obj
                    else:
                        fun(node.left, val)
                else:
                    if node.right is None:
                        node.right = obj
                    else:
                        fun(node.right, val)
            else:
                self.root = obj

        return fun(_node, value)

    def count(self):
        _node = self.root

        def fun(node):
            if node is None:
                return 0
            return 1 + fun(node.left) + fun(node.right)

        return fun(_node)

    def inorder(self):
        _node = self.root

        def fun(node, result: list):
            if node is not None:
                fun(node.left, result)
                result.append(node.value)
                fun(node.right, result)
            return result

        return fun(_node, [])

    def preorder(self):
        _node = self.root

        def fun(node, result: list):
            if node is not None:
                result.append(node.value)
                fun(node.left, result)
                fun(node.right, result)
            return result

        return fun(_node, [])

    def postorder(self):
        _node = self.root

        def fun(node, result: list):
            if node is not None:
                fun(node.left, result)
                fun(node.right, result)
                result.append(node.value)
            return result

        return fun(_node, [])

    def traverse_diagonal_elements(self):
        _node = self.root

        def fun(node, diagonal, d):
            if node is None:
                return
            d.setdefault(diagonal, []).append(node.value)
            fun(node.left, diagonal + 1, d)
            fun(node.right, diagonal, d)

        d = {}
        fun(_node, 0, d)
        return [d.get(di) for di in range(len(d))]

    def boundary_traversal(self):
        _node = self.root

        def leftBoundary(root):
            if root is None:
                return
            result = []
            while not root.isLeaf():
                result.append(root.value)
                root = root.left if root.left else root.right
            return result

        def rightBoundary(node):
            result = []

            def fun(root, result):
                if root is None or root.isLeaf():
                    return
                fun(root.right if root.right else root.left, result)
                result.append(root.value)

            fun(node, result)
            return result

        def leafNodes(node):
            result = []

            def fun(root, result: list):
                if root is None:
                    return
                fun(root.left, result)
                if root.isLeaf():
                    result.append(root.value)
                fun(root.right, result)

            fun(node, result)
            return result

        if _node is None:
            return
        boundary_nodes = [_node.value]
        boundary_nodes += leftBoundary(_node.left)
        if not _node.isLeaf():
            boundary_nodes += leafNodes(_node)
        boundary_nodes += rightBoundary(_node.right)
        return boundary_nodes

    def search(self, value):
        node = self.root
        while node is not None:
            if node.value == value:
                return node.value
            if node.value > value:
                node = node.left
            else:
                node = node.right
        return False


if __name__ == '__main__':
    tree = BinaryTree()
    lst = [10, 5, 12, 2, 7, 11, 15]
    for i in lst:
        tree.add_node(i)
    # print(tree.search(30))
    # print(tree.count())
    print(f"Inorder \t: {tree.inorder()}")
    print(f"Preorder\t: {tree.preorder()}")
    print(f"Postorder\t: {tree.postorder()}")
    print(f"Diagonal traversal\t: {tree.traverse_diagonal_elements()}")
    print(f"Boundary traversal\t: {tree.boundary_traversal()}")
