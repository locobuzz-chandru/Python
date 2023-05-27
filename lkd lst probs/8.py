# Delete a Node in a Linked List: Given a node to delete in a singly linked list, delete it in-place.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def delete_node(self, node):
        index = L.display().index(node)
        node = self.head.next
        prev = self.head
        for i in range(index - 1):
            node = node.next
            prev = prev.next
        prev.next = node.next
        node.next = None


if __name__ == '__main__':
    L = LinkedList()
    for i in range(1, 10):
        L.insert(i)
    print(L.display())
    L.delete_node(5)
    print(L.display())
