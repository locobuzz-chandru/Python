class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a linked list and print its elements
class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        values = []
        while current:
            values.append(current.data)
            current = current.next
        return values

    # Find the length of a linked list
    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Reverse a linked list
    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Check if a linked list is palindrome
    def is_palindrome(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        current = self.head
        while current:
            data = stack.pop()
            if current.data != data:
                return False
            current = current.next
        return True

    # Check if a linked list contains a given value
    def contains_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # Insert a new node at the beginning of a linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node from linked list
    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    # Find the middle node of a linked list
    def middle_node(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    # Remove duplicates from a sorted linked list
    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next


# Merge two sorted linked lists
def mergeTwoLists(head1, head2):
    if not head1 or not head2:
        return head1 if head1 else head2
    if head1.data > head2.data:
        head1, head2 = head2, head1
    head1.next = mergeTwoLists(head1.next, head2)
    return head1


if __name__ == '__main__':
    # obj = LinkedList()
    # for i in [1, 2, 3, 4, 3, 2, 1]:
    #     obj.add_node(i)
    # print(obj.display())
    # print(obj.get_length())
    # obj.reverse_linked_list()
    # print(obj.display())
    # print(obj.contains_value(5))
    # obj.insert_at_beginning(0)
    # print(obj.display())
    # obj.delete_node(5)
    # print(obj.display())
    # print(obj.middle_node())
    # print(obj.is_palindrome())
    l1 = LinkedList()
    for i in [1, 3, 4, 5, 7]:
        l1.add_node(i)
    l2 = LinkedList()
    for i in [2, 4, 6, 8]:
        l2.add_node(i)
    l1.display()
    l1.head = mergeTwoLists(l1.head, l2.head)
    print(l1.display())
    l1.remove_duplicates()
    print(l1.display())
