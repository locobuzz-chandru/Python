# Reverse a Linked List: Given a singly linked list, reverse it in-place.
# Detect a Cycle in a Linked List: Determine if a linked list contains a cycle and return the starting node of the cycle
# if present.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if not self.head:
            new.next = self.head
            self.head = new
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new

    def items(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst

    def reverse(self):
        node = self.head
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        self.head = prev


if __name__ == '__main__':
    l = LinkedList()
    for i in [1, 2, 3, 4, 5, 6]:
        l.insert(i)
    print(l.items())
    l.reverse()
    print(l.items())
