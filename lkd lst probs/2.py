# Find the Middle of a Linked List: Find the middle node of a linked list in a single pass.
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

    def items(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.data)
            node = node.next
        return lst

    def middle_element(self):
        slow = self.head
        fast = self.head
        if self.head is not None:
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow.data


if __name__ == '__main__':
    l = LinkedList()
    for i in [1, 2, 3, 4, 5, 6]:
        l.insert(i)
    print(l.items())
    print(l.middle_element())
