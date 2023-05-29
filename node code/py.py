class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNodeAtTail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return self.head

list = LinkedList()
list.insertNodeAtTail(141)
list.insertNodeAtTail(142)
list.insertNodeAtTail(143)

current = list.head
while current:
    print(current.data, end='>')
    current = current.next
    