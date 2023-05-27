# Merge Two Sorted Linked Lists: Given two sorted linked lists, merge them into a single sorted linked list.
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


def mergeTwoLists(head1, head2):
    if not head1 or not head2:
        return head1 if head1 else head2
    if head1.data > head2.data:
        head1, head2 = head2, head1
    head1.next = mergeTwoLists(head1.next, head2)
    return head1


if __name__ == '__main__':
    l1 = LinkedList()
    for i in [1, 3, 5, 7]:
        l1.insert(i)
    print(l1.display())
    l2 = LinkedList()
    for i in [0, 2, 4, 6, 8, 9]:
        l2.insert(i)
    print(l2.display())
    l1.head = mergeTwoLists(l1.head, l2.head)
    print(l1.display())
