# Remove Nth Node from the End of a Linked List: Remove the nth node from the end of a linked list and return the
# updated list.
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

    def delete_at_tail(self):
        node = self.head.next
        prev = self.head
        while node.next is not None:
            node = node.next
            prev = prev.next
        prev.next = None


if __name__ == '__main__':
    l = LinkedList()
    for i in [1, 2, 3, 4, 5, 6, 7]:
        l.insert(i)
    print(l.display())
    l.delete_at_tail()
    print(l.display())
