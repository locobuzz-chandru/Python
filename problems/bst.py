class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self._id = value.id


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def add(self, value):
        obj = TreeNode(value)
        _node = self.root

        def fun(node, val):
            if node is not None:
                if val.id < node._id:
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

    def traverse_inorder(self):
        _node = self.root

        def fun(node, result: list):
            if node is not None:
                fun(node.left, result)
                result.append(node.value)
                fun(node.right, result)
            return result

        return fun(_node, [])

    def search(self, task_id):
        node = self.root
        while node is not None:
            if node._id == task_id:
                return node.value
            if node._id > task_id:
                node = node.left
            else:
                node = node.right
        return False
