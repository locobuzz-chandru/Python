# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even
# indices
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

    def odd_even(self):
        odd = self.head
        even = self.head.next
        even_head = even
        while even and even.next:
            odd.next = even.next  # 1->3
            odd = odd.next  # 3
            even.next = odd.next  # 2->4
            even = even.next  # 4
        odd.next = even_head  # 5->2


if __name__ == '__main__':
    L = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        L.insert(i)
    print(L.display())
    L.odd_even()
    print(L.display())
