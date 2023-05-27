# Intersection of Two Linked Lists: Find the intersection point of two linked lists, if any.
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst


def find_intersection(head1, head2):
    nodes = []
    while head1:
        nodes.append(head1.data)
        head1 = head1.next
    while head2:
        if head2.data in nodes:
            return head2.data
        head2 = head2.next
    return None


if __name__ == '__main__':
    l1 = LinkedList()
    for i in range(1, 6):
        l1.insert(i)
    print(l1.display())
    l2 = LinkedList()
    for i in range(1, 4):
        l2.insert(i)
    print(l2.display())
    intersection = find_intersection(l1.head, l2.head)
    print(intersection)
