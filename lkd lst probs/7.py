# Add Two Numbers Represented by Linked Lists: Given two linked lists representing numbers, add them and return the sum
# as a linked list.
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


def add_linked_lists(head1, head2):
    l1 = []
    l2 = []
    while head1:
        l1.append(head1.data)
        head1 = head1.next
    while head2:
        l2.append(head2.data)
        head2 = head2.next
    s1 = ''.join(l1)
    s2 = ''.join(l2)
    s = int(s1) + int(s2)
    for i in list(str(s)):
        l.insert(i)


if __name__ == '__main__':
    l1 = LinkedList()
    for i in '369':
        l1.insert(i)
    # print(l1.display())
    l2 = LinkedList()
    for i in '31':
        l2.insert(i)
    # print(l2.display())
    l = LinkedList()
    add_linked_lists(l1.head, l2.head)
    print(l.display())
