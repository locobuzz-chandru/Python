class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            node = self.head
            while node:
                print(node.data, "--> ", end='')
                node = node.next
            print('\n')

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node

    def insert_at_index(self, index, data):
        new_node = Node(data)
        node = self.head
        for i in range(index - 1):
            node = node.next
        new_node.next = node.next
        node.next = new_node

    def delete_at_head(self):
        node = self.head
        self.head = node.next
        node.next = None

    def delete_at_tail(self):
        node = self.head.next
        prev = self.head
        while node.next is not None:
            node = node.next
            prev = prev.next
        prev.next = None

    def delete_at_index(self, index):
        node = self.head.next
        prev = self.head
        for i in range(index - 1):
            node = node.next
            prev = prev.next
        prev.next = node.next
        node.next = None


L = SingleLinkedList()
L.insert_at_head(20)
L.insert_at_tail(30)
L.insert_at_tail(40)
L.insert_at_tail(60)
L.insert_at_head(10)
L.insert_at_index(4, 50)
L.display()
# L.delete_at_head()
# L.display()
# L.delete_at_tail()
# L.display()
# L.delete_at_index(3)
# L.display()
