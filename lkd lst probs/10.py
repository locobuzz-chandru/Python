# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from
# the end (the list is 1-indexed).
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def display(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst

    def swap_nodes(self, k):
        first = last = self.head
        for i in range(1, k):
            first = first.next
        ptr = first
        while ptr.next:
            last = last.next
            ptr = ptr.next
        first.data, last.data = last.data, first.data


if __name__ == '__main__':
    L = LinkedList()
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        L.insert(i)
    print(L.display())
    L.swap_nodes(3)
    print(L.display())
