# Given the head of a sorted linked list, delete all duplicates such that each element appears only once
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

    def remove_duplicates(self):
        if not self.head:
            return None
        node = self.head
        while node.next:
            if node.data == node.next.data:
                node.next = node.next.next
            else:
                node = node.next


if __name__ == '__main__':
    L = LinkedList()
    for i in [1, 2, 3, 3, 4]:
        L.insert(i)
    print(L.display())
    L.remove_duplicates()
    print(L.display())
